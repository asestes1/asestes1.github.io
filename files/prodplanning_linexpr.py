import gurobipy
import numpy

# Input some problem parameters:
materials_avail = [30.0, 42.0, 56.0]
revenues = [1.0, 3.0, 4.0, 2.0, 1.0]
# materials_used[i,j] stores the material i used by product j
materials_used = numpy.array([[1.0, 1.0, 0.0, 2.0, 5.0],
                             [2.0, 0.0, 0.0, 1.0, 7.0],
                             [0.0, 2.0, 4.0, 0.0, 0.0]])

num_materials, num_items = materials_used.shape

model = gurobipy.Model()

# This returns a dictionary; prods_produced[i] will be the variable storing the
# quantity of product i that is produced.
prods_produced = model.addVars(len(revenues), lb=0.0, ub=gurobipy.GRB.INFINITY)

# This is the loop for adding constraints:
for i in range(0, len(materials_avail)):
    # Create an empty linear expression object that will hold the left-hand-side
    lhs = gurobipy.LinExpr()
    for j in range(0, len(revenues)):
        # Add the relevant variables with the appropriate coefficients
        lhs.add(prods_produced[j], materials_used[i, j])
    # Add the constraint.
    model.addConstr(lhs <= materials_avail[i])

# Also create
obj = gurobipy.LinExpr()
for j, profit_j in enumerate(revenues):
    obj.add(prods_produced[j], profit_j)

model.setObjective(obj, sense=gurobipy.GRB.MAXIMIZE)

model.optimize()
status = model.getAttr("Status")
if status == gurobipy.GRB.OPTIMAL:
    for var_index, myvar in prods_produced.items():
        print("Product " + str(var_index) + ":", myvar.X)
    # model.getAttr("ObjVal") and model.ObjVal both get the objective value.
    print(model.getAttr("ObjVal"))
    print(model.ObjVal)
else:
    print("No optimal solution found.")
