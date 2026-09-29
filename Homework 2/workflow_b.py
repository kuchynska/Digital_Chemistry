import json
import os
import csv
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

os.makedirs("output_b", exist_ok=True)

with open("fragments.json", "r") as file:
    data = json.load(file)

scaffold = data["scaffold"]
fragments = data["fragments"]

print("Scaffold:", scaffold["name"], scaffold["smiles"])

for fragment in fragments:
    print("Fragment:", fragment["name"], fragment["smiles"])
products = []

for fragment in fragments:
    scaffold_mol = Chem.MolFromSmiles(scaffold["smiles"])
    fragment_mol = Chem.MolFromSmiles(fragment["smiles"])

    combined = Chem.CombineMols(scaffold_mol, fragment_mol)
    editable = Chem.RWMol(combined)

    dummy_atoms = [
        atom.GetIdx()
        for atom in editable.GetAtoms()
        if atom.GetAtomicNum() == 0
    ]

    dummy1 = dummy_atoms[0]
    dummy2 = dummy_atoms[1]

    neighbor1 = editable.GetAtomWithIdx(dummy1).GetNeighbors()[0].GetIdx()
    neighbor2 = editable.GetAtomWithIdx(dummy2).GetNeighbors()[0].GetIdx()

    editable.AddBond(neighbor1, neighbor2, Chem.BondType.SINGLE)

    for idx in sorted(dummy_atoms, reverse=True):
        editable.RemoveAtom(idx)

    product = editable.GetMol()
    Chem.SanitizeMol(product)

    product_name = "phenyl_" + fragment["name"]
    product_smiles = Chem.MolToSmiles(product)

    products.append({
        "name": product_name,
        "smiles": product_smiles,
        "mol": product
    })

    print(product_name, ":", product_smiles)
    mol_path = os.path.join("output_b", product_name + ".mol")
    Chem.MolToMolFile(product, mol_path)

    png_path = os.path.join("output_b", product_name + ".png")
    Draw.MolToFile(product, png_path)
    product_3d = Chem.AddHs(product)

    AllChem.EmbedMolecule(product_3d, randomSeed=42)
    AllChem.UFFOptimizeMolecule(product_3d)

    mol_3d_path = os.path.join("output_b", product_name + "_3d.mol")
    Chem.MolToMolFile(product_3d, mol_3d_path)

    xyz_path = os.path.join("output_b", product_name + ".xyz")
    Chem.MolToXYZFile(product_3d, xyz_path)
sdf_path = os.path.join("output_b", "fragment_library.sdf")
writer = Chem.SDWriter(sdf_path)
for item in products:
    mol = Chem.Mol(item["mol"])
    mol.SetProp("_Name", item["name"])
    mol.SetProp("Canonical_SMILES", item["smiles"])
    writer.write(mol)

writer.close()
summary_path = os.path.join("output_b", "summary.csv")

with open(summary_path, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["name", "canonical_smiles"])

    for item in products:
        csv_writer.writerow([item["name"], item["smiles"]])