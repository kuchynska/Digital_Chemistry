import json
import os
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
import pubchempy as pcp
os.makedirs("output", exist_ok=True)
with open("molecules.json", "r") as file:
    molecules = json.load(file)
print(molecules)
first_molecule = molecules[0]
mol = Chem.MolFromSmiles(first_molecule["smiles"])
print(first_molecule["name"])
print(mol)
canonical_smiles = Chem.MolToSmiles(mol)
print(canonical_smiles)
inchi = Chem.MolToInchi(mol)
print(inchi)
inchikey = Chem.MolToInchiKey(mol)
print(inchikey)
for molecule in molecules:
    print(molecule["name"])
    mol = Chem.MolFromSmiles(molecule["smiles"])
    print(mol)
    canonical_smiles = Chem.MolToSmiles(mol)
    print(canonical_smiles)
    inchi = Chem.MolToInchi(mol)
    print(inchi)
    inchikey = Chem.MolToInchiKey(mol)
    print(inchikey)
    mol_path = os.path.join("output", molecule["name"] + ".mol")
    Chem.MolToMolFile(mol, mol_path)
    png_path = os.path.join("output", molecule["name"] + ".png")
    Draw.MolToFile(mol, png_path)
    mol_3d = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol_3d, randomSeed=42)
    AllChem.UFFOptimizeMolecule(mol_3d)
    mol_3d_path = os.path.join("output", molecule["name"] + "_3d.mol")
    Chem.MolToMolFile(mol_3d, mol_3d_path)
    xyz_path = os.path.join("output", molecule["name"] + ".xyz")
    Chem.MolToXYZFile(mol_3d, xyz_path)
sdf_path = os.path.join("output", "molecules.sdf")
writer = Chem.SDWriter(sdf_path)
for molecule in molecules:
    mol = Chem.MolFromSmiles(molecule["smiles"])
    mol.SetProp("_Name", molecule["name"])
    writer.write(mol)
writer.close()
compounds = pcp.get_compounds("water", "name")
print(compounds)
compound = compounds[0]
print(compound.cid)
print(compound.molecular_formula)
print(compound.molecular_weight)
print(compound.xlogp)
for molecule in molecules:
    print(molecule["name"])
    compounds = pcp.get_compounds(molecule["name"].replace("_", " "), "name")
    if compounds:
        compound = compounds[0]
        molecule["pubchem_cid"] = str(compound.cid)
        molecule["pubchem_formula"] = compound.molecular_formula
        molecule["pubchem_molecular_weight"] = str(compound.molecular_weight)
        molecule["pubchem_xlogp"] = str(compound.xlogp)
        print("CID:", compound.cid)
        print("Formula:", compound.molecular_formula)
        print("Molecular weight:", compound.molecular_weight)
        print("XLogP:", compound.xlogp)
sdf_path = os.path.join("output", "molecules_with_pubchem.sdf")
writer = Chem.SDWriter(sdf_path)
for molecule in molecules:
    mol = Chem.MolFromSmiles(molecule["smiles"])
    mol.SetProp("_Name", molecule["name"])
    if "pubchem_cid" in molecule:
        mol.SetProp("PubChem_CID", molecule["pubchem_cid"])
        mol.SetProp("Molecular_Formula", molecule["pubchem_formula"])
        mol.SetProp("Molecular_Weight", molecule["pubchem_molecular_weight"])
        mol.SetProp("XLogP", molecule["pubchem_xlogp"])
    writer.write(mol)
writer.close()