import gurobipy

nodes = range(1, 8)
edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)]
colors = [1, 2, 3, 4]
model = gurobipy.Model()

nodecolors = {(node, color): model.addVar(vtype=gurobipy.GRB.BINARY) for node in nodes for color in colors}
color_usage = {c: model.addVar(vtype=gurobipy.GRB.BINARY) for c in colors}

model.addConstrs(
    (nodecolors[node_a, color] + nodecolors[node_b, color] <= 1
     for (node_a, node_b) in edges for color in colors)
)

model.addConstrs(
    (nodecolors[node, color] <= color_usage[color]
     for node in nodes for color in colors)
)

model.addConstrs(
    (gurobipy.quicksum(nodecolors[node, color] for color in colors) == 1 for node in nodes)
)

model.setObjective(gurobipy.quicksum(color_usage[color] for color in colors), sense=gurobipy.GRB.MINIMIZE)

model.optimize()

status = model.getAttr("Status")
if status == 2:
    print("Number of colors used: ", model.getAttr("ObjVal"))
    for v in nodes:
        for c in colors:
            if nodecolors[v, c].getAttr("X") == 1:
                print("Node "+str(v)+", color: ", c)
else:
    print("No optimal solution found.")
