import csv
import json
with open("molecules.json", "r") as file:
    molecules = json.load(file)
print(len(molecules))

reactions = []

with open("rxn.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reactions.append(row)

print(reactions)

with open("rxn-detail.csv", "r") as file:
    reader = csv.DictReader(file)

    for detail in reader:
        for reaction in reactions:
            if reaction["reaction_id"] == detail["reaction_id"]:
                reaction.update(detail)

print(reactions)

nodes = []

for molecule in molecules:
    nodes.append({
        "id": molecule["molecule_id"],
        "label": molecule["name"]
    })

print(nodes)

print(reactions[0].keys())
edges = []

for reaction in reactions:
    edges.append({
        "id": reaction["reaction_id"],
        "source": reaction["source"],
        "target": reaction["target"],
        "reaction_type": reaction["reaction_type"],
        "equation": reaction["equation"],
        "yield_percent": reaction["yield_percent"],
        "temperature_C": reaction["temperature_C"]
    })

print(edges)

network = {
    "nodes": nodes,
    "edges": edges
}

with open("rxn-net.json", "w") as file:
    json.dump(network, file, indent=4)

    import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

for node in nodes:
    G.add_node(node["id"], label=node["label"])

for edge in edges:
    G.add_edge(
        edge["source"],
        edge["target"],
        reaction_type=edge["reaction_type"]
    )
  



labels = nx.get_node_attributes(G, "label")
edge_labels = {
    ("M001", "M002"): "oxidation",
    ("M002", "M003"): "oxidation",
    ("M001", "M004"): "dehydration"
}

pos = {
    "M001": (0, 0),       # Ethanol

    "R001": (0, -1),
    "M002": (0, -2),      # Acetaldehyde
    "R002": (0, -3),
    "M003": (0, -4),      # Acetic acid

    "R003": (2, 0),
    "M004": (3, -1),      # Ethene
    "M005": (3, 1)        # Water
}


nx.draw(G, pos, with_labels=True, labels=labels, arrows=True)
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)
plt.text(
    3, 0,
    "+",
    fontsize=20,
    ha="center",
    va="center"
)

plt.savefig("rxn-net.png")
plt.close()

start_molecule = "M001"

products = []

for edge in edges:
    if edge["source"] == start_molecule:
        for node in nodes:
           if node["id"] == edge["target"]:
             products.append(node["label"])

print("Products reachable from Ethanol:", products)

high_yield_reactions = []

for edge in edges:
    if float(edge["yield_percent"]) > 90:
       if edge["id"] not in high_yield_reactions:
          high_yield_reactions.append(edge["id"])

print("Reactions with yield > 90%:", high_yield_reactions)