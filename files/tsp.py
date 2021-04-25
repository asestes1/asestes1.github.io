import random
import math
import gurobipy
import typing

# generate some random points.
npts = 50
random.seed(1)
points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(npts)]


def dist(pointA: typing.Tuple[float, float], pointB: typing.Tuple[float, float]):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


def find_subtour(sol: typing.Dict[typing.Tuple[int, int], float], n: int) -> typing.List[int]:
    """
    This function takes a a solution to the TSP formulation, and returns a subtour.
    :param sol: a dict, each key is a two-tuple (i,j) with i < j and sol[i,j] gives the value of the variable
                corresponding to the edge between i and j
    :param n: the number of nodes.
    :return: a subtour in the TSP formulation, starting with node 0. This returns a list of the nodes in the subtour.
    """
    start_node = 0
    prev_node = None
    current_node = start_node
    returned_to_start = False
    cycle = [start_node]
    while not returned_to_start:
        next_node = None
        for j in range(current_node + 1, n):
            if sol[current_node, j] > 0.5 and j != prev_node:
                next_node = j
        if next_node is None:
            for j in range(0, current_node):
                if sol[j, current_node] > 0.5 and j != prev_node:
                    next_node = j
        if next_node is None:
            raise RuntimeError("Failed to find subtour")
        elif next_node == start_node:
            returned_to_start = True
        else:
            cycle.append(next_node)
        prev_node = current_node
        current_node = next_node
    return cycle


mymodel = gurobipy.Model()
mymodel.params.lazyConstraints = 1  # You have to set this parameter if you're going to use callbacks to add constraints.
mymodel.ModelSense = gurobipy.GRB.MINIMIZE

myvars = {}
for i in range(0, npts):
    for j in range(i + 1, npts):
        myvars[i, j] = mymodel.addVar(obj=dist(points[i], points[j]), vtype=gurobipy.GRB.BINARY)

for i in range(npts):
    adj = gurobipy.quicksum(myvars[i, j] for j in range(i + 1, npts)) + gurobipy.quicksum(
        myvars[j, i] for j in range(0, i))
    mymodel.addConstr(adj == 2)
mymodel.update()


# This is the gurobi callback function. The callback method must have two arguments, model and where
# "where" tells the callback function what event caused the callback to be called
def subtourelim(model, where):
    # If something other than a MIP solution invoked the callback function, we don't do anything
    if where != gurobipy.GRB.Callback.MIPSOL:
        return

    # cbGetSolution gets the latest MIP solution from the model
    # this can only be used when "where" is equal to gurobipy.GRB.Callback.MIPSOL or GRB.
    # This takes as an argument a dictionary of variables, and returns a dictionary of values with the same keys.
    vals = model.cbGetSolution(myvars)
    subtour = find_subtour(vals, npts)
    if len(subtour) < npts:
        model.cbLazy(gurobipy.quicksum(myvars[i, j] for i in subtour for j in subtour if i < j) <= len(subtour) - 1)
    return


# This syntax tells the model to optimize, using the function subtourelim as the callback.
mymodel.optimize(subtourelim)
mysol = {(i, j): myvars[i, j].X for i in range(0, npts) for j in range(i + 1, npts)}
print("Best solution: ", find_subtour(mysol, npts))
