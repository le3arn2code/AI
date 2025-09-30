import matplotlib.pyplot as plt
import networkx as nx

# Define a simple NN: 3 inputs -> 2 hidden -> 1 output
G = nx.DiGraph()

# Layers
input_nodes = ["I1", "I2", "I3"]
hidden_nodes = ["H1", "H2"]
output_nodes = ["O1"]

# Add edges (fully connected)
for i in input_nodes:
    for h in hidden_nodes:
        G.add_edge(i, h)
for h in hidden_nodes:
    for o in output_nodes:
        G.add_edge(h, o)

# Position nodes in layers
pos = {
    "I1": (0, 0), "I2": (0, -1), "I3": (0, -2),
    "H1": (2, -0.5), "H2": (2, -1.5),
    "O1": (4, -1)
}

plt.figure(figsize=(6,4))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", arrows=True)
plt.title("Simple Neural Network Diagram")
plt.savefig("neural_network_diagram.png")
print("✅ Diagram saved as neural_network_diagram.png")
