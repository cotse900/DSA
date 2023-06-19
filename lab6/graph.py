import networkx as nx
import matplotlib.pyplot as plt

# Define graph edges and weights
edges = [('A', 'B', 2), ('A', 'C', 1), ('B', 'C', 2), ('B', 'D', 1),
         ('C', 'D', 4), ('C', 'E', 3), ('D', 'E', 1), ('D', 'F', 2),
         ('E', 'F', 1), ('F', 'G', 3)]

# Create a directed graph object
G = nx.DiGraph()

# Add edges to the graph object
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Draw the graph with node labels and edge weights
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()