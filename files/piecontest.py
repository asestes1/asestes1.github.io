import gurobipy

# If you don't want to write "gurobipy" to access the Gurobi interface:
# import gurobiby as *

my_model = gurobipy.Model()

torte_var = my_model.addVar(lb=0.0,  # lb defaults to zero, so this can be removed.
                            ub=gurobipy.GRB.INFINITY,  # ub defaults to infinity, so this can be removed.
                            vtype=gurobipy.GRB.CONTINUOUS,
                            name="Tortes")
pie_var = my_model.addVar(vtype=gurobipy.GRB.CONTINUOUS, name="Pies")

# # Alternative method, multiple variables created at once:
# my_vars = my_model.addVars(2, vtype=gurobipy.GRB.CONTINUOUS, name=["Tortes", "Pies"])
#
# # Accessing individual variables:
# torte_var = my_vars[0]
# pie_var = my_vars[1]

my_model.setObjective(4 * torte_var + 5 * pie_var,
                      sense=gurobipy.GRB.MAXIMIZE)  # gurobipy.GRB.MINIMIZE for minimization problems

my_model.addConstr(2 * torte_var + 3 * pie_var <= 60.0, name=" MyConstr ")

my_model.optimize()
print(my_model.getAttr("Status"))
print("Tortes:", torte_var.getAttr("X"))
print("Pies:", pie_var.getAttr("X"))
