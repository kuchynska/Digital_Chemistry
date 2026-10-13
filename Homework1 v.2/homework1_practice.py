import csv
import json
import networkx as nx
import matplotlib.pyplot as plt

molecules = {}

with open("Homework1 v.2/molecules.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        molecule_id = row["molecule_id"]
        molecules[molecule_id] = row

#Add properties to molecules

with open("Homework1 v.2/properties.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        molecule_id = row["molecule_id"]
        molecules[molecule_id]["properties"] = row

print(molecules["M001"])

#Add safety information to molecules

with open("Homework1 v.2/safety.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        molecule_id = row["molecule_id"]
        molecules[molecule_id]["safety"] = row

print(molecules["M001"])
for molecule_id, data in molecules.items():
    print(molecule_id, data)

# Save molecules as JSON

with open("Homework1 v.2/molecules.json", "w", encoding="utf-8") as file:
    json.dump(molecules, file, indent=4)

# Check the JSON file

with open("Homework1 v.2/molecules.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Number of molecules:", len(data))
print("M001:", data["M001"]["name"])
print("Properties:", "properties" in data["M001"])
print("Safety:", "safety" in data["M001"])

#Part B - Network

#Create a dictionary of reactions

reactions = {}

with open("Homework1 v.2/rxn.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reaction_id = row["reaction_id"]
        reactions[reaction_id] = row

print("Number of reactions:", len(reactions))
print("First reaction:", reactions["R001"])

#Add reaction details

with open("Homework1 v.2/rxn-detail.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reaction_id = row["reaction_id"]
        reactions[reaction_id]["details"] = row

print(reactions["R001"])

#Create nodes for the reaction network

nodes = []

for molecule_id, data in molecules.items():
    node = {
        "id": molecule_id,
        "label": data["name"]
    }

    nodes.append(node)

print("Number of nodes:", len(nodes))
print("First node:", nodes[0])

# Create edges for the reaction network

edges = []

for reaction_id, data in reactions.items():
    edge = {
        "id": reaction_id,
        "source": data["source_id"],
        "target": data["target_id"],
        "reaction_type": data["reaction_type"],
        "equation": data["equation"],
        "details": data["details"]
    }

    edges.append(edge)

print("Number of edges:", len(edges))
print("First edge:", edges[0])

# Create the reaction network

network = {
    "nodes": nodes,
    "edges": edges
}

#Save the reaction network as JSON

with open("Homework1 v.2/rxn-net.json", "w", encoding="utf-8") as file:
    json.dump(network, file, indent=4)

print("Reaction network saved successfully!")



#VISUALISE REACTION NETWORK


# Create a directed graph
G = nx.DiGraph()

# Add molecules as nodes
for node in nodes:
    G.add_node(node["id"], label=node["label"])

# Add reactions as edges
for edge in edges:
    G.add_edge(edge["source"], edge["target"])

# Define positions of the nodes
pos = nx.spring_layout(G, seed=42, k=2, iterations=200)

# Create the graph image
plt.figure(figsize=(14, 10))

# Show molecule names instead of IDs
labels = nx.get_node_attributes(G, "label")

nx.draw(
    G,
    pos,
    labels=labels,
    with_labels=True,
    node_color="lightblue",
    node_size=1700,
    font_size=7,
    arrows=True,
    arrowsize=15,
    edge_color="gray"
)


# Save the image
plt.savefig("Homework1 v.2/rxn-net.png", dpi=300, bbox_inches="tight")
plt.close()


#PART C - QUERY / FILTER
#Find reactions by reaction type
# PART C - QUERY / FILTER

def find_reactions(reaction_type):
    for edge in edges:
        if edge["reaction_type"] == reaction_type:
            print(edge["id"], edge["equation"])

find_reactions("oxidation")

print("PART C FINISHED")


#Сheck network

print("Nodes:", len(network["nodes"]))
print("Edges:", len(network["edges"]))

node_ids = [node["id"] for node in network["nodes"]]

for edge in network["edges"]:
    if edge["source"] not in node_ids or edge["target"] not in node_ids:
        print("Unknown molecule in reaction:", edge["id"])

print("Network check finished!")