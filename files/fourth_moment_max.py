import gurobipy

K = 5
first_moment = 3.5
second_moment = 15

my_model = gurobipy.Model()
my_vars = my_model.addVars(K, lb=0, ub=1)
constr = my_model.addConstr(gurobipy.quicksum(my_vars[k] for k in range(0, K)) == 1)
constr = my_model.addConstr(gurobipy.quicksum(k * my_vars[k - 1] for k in range(1, K + 1)) == first_moment)
constr = my_model.addConstr(gurobipy.quicksum((k ** 2) * my_vars[k - 1] for k in range(1, K + 1)) == second_moment)
my_model.setObjective(gurobipy.quicksum((k ** 4) * my_vars[k - 1] for k in range(1, K + 1)),
                      gurobipy.GRB.MAXIMIZE)

my_model.optimize()

if my_model.getAttr("Status") == gurobipy.GRB.OPTIMAL:
    for i in range(0, K):
        print("Pr(X = " + str(i + 1) + ")=" + str(my_vars[i].getAttr("X")))
    print("Fourth moment: ", my_model.getAttr("ObjVal"))
else:
    print("Not optimal. Gurobi status code: ", my_model.getAttr("Status"))
