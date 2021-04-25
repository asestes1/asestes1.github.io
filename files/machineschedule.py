import gurobipy
import itertools

n_items = 7
processing_times = [5, 10, 17, 8, 9, 14, 28]
deadlines = [60, 20, 32, 27, 44, 52, 77]
penalties = [10, 18, 14, 89, 22, 37, 46]

model = gurobipy.Model()
model.ModelSense = gurobipy.GRB.MINIMIZE

#completion_vars[i] stores x[i]
completion_vars = model.addVars(n_items, vtype=gurobipy.GRB.CONTINUOUS, obj=0.0, lb=processing_times)

# complete_order_vars[i,j,k] will store x_{ij}^k
complete_order_vars = {(i, j, k): model.addVar(vtype=gurobipy.GRB.CONTINUOUS, obj=0.0, lb=0.0)
                       for i in range(0, n_items) for j in range(0, n_items) if i != j
                       for k in {i, j}}
# order_vars[i,j] stores y_{ij}
order_vars = {(i, j): model.addVar(vtype=gurobipy.GRB.BINARY, obj=0.0)
              for i in range(0, n_items) for j in range(0, n_items) if i != j}
penalty_vars = model.addVars(n_items, vtype=gurobipy.GRB.CONTINUOUS, obj=penalties, lb=0.0)
model.update()

for i, j in itertools.combinations(range(0, n_items), 2):
    model.addConstr(order_vars[i, j] + order_vars[j, i] == 1)

total_time = sum(processing_times)
for i in range(0, n_items):
    for j in range(0, n_items):
        if i != j:
            model.addConstr(complete_order_vars[i, j, i] <= total_time * order_vars[i, j])
            model.addConstr(complete_order_vars[j, i, i] <= total_time * order_vars[j, i])
            model.addConstr(complete_order_vars[i,j, j] >= complete_order_vars[i,j,i]
                            +processing_times[j]*order_vars[i,j])
            model.addConstr(completion_vars[i] == complete_order_vars[i,j,i] + complete_order_vars[j,i,i])

for i in range(0, n_items):
    model.addConstr(penalty_vars[i] >= completion_vars[i] - deadlines[i])
model.update()

model.optimize()

for i, v in completion_vars.items():
    print(i+1, v.X)
