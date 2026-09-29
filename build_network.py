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
    G.add_edge(edge["source"], edge["target"])

labels = nx.get_node_attributes(G, "label")

nx.draw(G, with_labels=True, labels=labels, arrows=True)
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