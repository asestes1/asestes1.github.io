import random
import math
import gurobipy
import typing

# generate some random points.
npts = 100
random.seed(1)
points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(npts)]


def dist(pointA, pointB):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


"""
This function takes a a solution to the TSP formulation, and returns a subtour.

sol: a list of two-element integer tuples (i,j) with i < j
n: the number of nodes.

:return a subtour in the TSP formulation, starting with node 0
"""
def find_subtour(sol: typing.Dict[typing.Tuple[int, int], float], n: int) -> typing.Optional[
    typing.List[typing.Tuple[int, int]]]:
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
                cycle.append(next_node)
        if next_node is None:
            for j in range(0, current_node):
                if sol[j, current_node] > 0.5 and j != prev_node:
                    next_node = j
                    cycle.append(next_node)
        if next_node is None:
            raise RuntimeError("Failed to find subtour")
        elif next_node == start_node:
            returned_to_start = True
        prev_node = current_node
        current_node = next_node
    return cycle


mymodel = gurobipy.Model()
mymodel.params.lazyConstraints = 1
mymodel.ModelSense = gurobipy.GRB.MINIMIZE

vars = {}
for i in range(0, npts):
    for j in range(i + 1, npts):
        vars[i, j] = mymodel.addVar(obj=dist(points[i], points[j]), vtype=gurobipy.GRB.BINARY)

for i in range(npts):
    adj = gurobipy.quicksum(vars[i, j] for j in range(i + 1, npts)) + gurobipy.quicksum(vars[j, i] for j in range(0, i))
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
    vals = model.cbGetSolution(vars)
    subtour = find_subtour(vals, npts)
    if len(subtour) < npts:
        model.cbLazy(gurobipy.quicksum(vars[i, j] for i in subtour for j in subtour if i < j) <= len(subtour) - 1)
    return


mymodel.optimize(subtourelim)
mysol = {(i,j): vars[i, j].X for i in range(0, npts) for j in range(i+1,npts)}
print("Best solution: ", find_subtour(mysol,npts))