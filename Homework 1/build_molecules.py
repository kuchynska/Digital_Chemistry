import csv
import json

molecules = {}

with open("molecules.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        molecules[row["molecule_id"]] = row
print(molecules)
with open("properties.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        molecule_id = row["molecule_id"]
        molecules[molecule_id]["properties"] = row
print(molecules)
with open("safety.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        molecule_id = row["molecule_id"]
        molecules[molecule_id]["safety"] = row
print(molecules)
with open("molecules.json", "w") as file:
    json.dump(list(molecules.values()), file, indent=4)