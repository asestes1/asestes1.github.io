import gurobipy
import numpy


# If you don't want to write ``gurobipy" to access the Gurobi interface:
# import gurobiby as *

# Input some problem parameters:
revenues = [1.0, 3.0, 4.0, 2.0, 1.0]
materials_req = numpy.array([[1.0, 1.0, 0.0, 2.0, 5.0],
                             [2.0, 0.0, 0.0, 1.0, 7.0],
                             [0.0, 2.0, 4.0, 0.0, 0.0]])
materials_avail = [30.0, 42.0, 56.0]
num_materials, num_items = materials_req.shape


mymodel = gurobipy.Model()

myvars = mymodel.addVars(num_items, lb=0.0, obj=revenues, vtype=gurobipy.GRB.CONTINUOUS)
mymodel.ModelSense = gurobipy.GRB.MAXIMIZE
mymodel.update() # may not be needed, depending on Gurobi version

# Form a generator that contains the constraints
constraints = (gurobipy.quicksum(materials_req[i, j] * myvars[j] for j in range(0, num_items)) <= materials_avail[i]
               for i in range(0, num_materials))
mymodel.addConstrs(constraints)
mymodel.update() # may not be needed, depending on Gurobi version

mymodel.optimize()
if mymodel.status == gurobipy.GRB.OPTIMAL:
    for i, myvar in myvars.items():
        print("Product "+str(i)+":", myvar.X)
    print("Total revenue: ", mymodel.ObjVal)
else:
    print("Gurobi didn't find an optimal solution.")