import gurobipy
import numpy

tol = 0.00001
y_points = [numpy.array([0.0, 0.0]), numpy.array([0.0, 2.0]), numpy.array([1.0, 1.0]),
            numpy.array([2.0, 2.0]), numpy.array([2.0, 0.0])]
z_points = [numpy.array([0.5, -0.5]), numpy.array([3.0, -2.0]), numpy.array([3.0, 2.0])]

dim = y_points[0].shape[0]

my_model = gurobipy.Model()
my_model.setParam("Method", 0)

point_x = my_model.addVars(dim, lb=0.0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS)
point_w = my_model.addVars(dim, lb=0.0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS)

error_r = my_model.addVars(dim, lb=0.0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS)
error_s = my_model.addVars(dim, lb=0.0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS)

convex_coeffs_alpha = my_model.addVars(len(y_points), lb=0.0, ub=1.0, vtype=gurobipy.GRB.CONTINUOUS)
convex_coeffs_beta = my_model.addVars(len(z_points), lb=0.0, ub=1.0, vtype=gurobipy.GRB.CONTINUOUS)

my_model.setObjective(gurobipy.quicksum(error_r) + gurobipy.quicksum(error_s), sense=gurobipy.GRB.MINIMIZE)

my_model.addConstrs(gurobipy.quicksum(convex_coeffs_alpha[i] * pt[j] for i, pt in enumerate(y_points)) == point_x[j]
                    for j in range(0, dim))
my_model.addConstr(gurobipy.quicksum(convex_coeffs_alpha) == 1)

my_model.addConstrs(gurobipy.quicksum(convex_coeffs_beta[i] * pt[j] for i, pt in enumerate(z_points)) == point_w[j]
                    for j in range(0, dim))
my_model.addConstr(gurobipy.quicksum(convex_coeffs_beta) == 1)

my_model.addConstrs(point_x[j] + error_r[j] == point_w[j] + error_s[j] for j in range(0, dim))
my_model.optimize()

if my_model.getAttr("ObjVal") > 0.00001:
    print("Convex hulls do not intersect.")
else:
    print("Convex hulls intersect.")
    print("Example Point: " + str(tuple(point_x[j].getAttr("X") for j in range(0, dim))))
