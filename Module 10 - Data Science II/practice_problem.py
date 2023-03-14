import pdb
import networkx as nx
import matplotlib.pyplot as plt

# Read in the data
with open('practice_problem_data.txt') as f:
    data = f.read()

# Create a Graph
graph = nx.DiGraph()

# Add Nodes
rows = data.split('\n')
nodes = rows[0].split()
graph.add_nodes_from(nodes)

# Add Edges
data_rows = rows[1:]
for i in data_rows:
    src = i.split()[0]
    weights = i.split()[1:]
    for index, dest in enumerate(nodes):
        weight = int(weights[index])
        if weight == 0:
            continue
        graph.add_edge(src, dest, weight=weight)

# Answer the questions
print("Question 1")
print(f'In-degree of "d": {graph.in_degree("d")}')
print(f'Predecessors of "d": {[p for p in graph.predecessors("d")]}')
print()

print("Question 2")
print(f'Out-degree of "g": {graph.out_degree("g")}')
print(f'Successors of "g": {[s for s in graph.successors("g")]}')
print()

print("Question 3")
connectivity = {}
for i in nodes:
    connectivity[i] = graph.in_degree(i) + graph.out_degree(i)
print(connectivity)
print()

print("Question 4")
print(f'Shortest path between "j" and "b": {nx.dijkstra_path(graph, "j", "b")}')
print()

# Draw the graph
print("Question 5")
nx.draw_networkx(graph, with_labels=True)
plt.show()
