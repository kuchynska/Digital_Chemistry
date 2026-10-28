import json
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import MolToFile
filename=input("Enter filename: ")
print(filename)
with open(filename) as file:
    data=json.load(file)  
print(data)
print(len(data))
print(data[0])
print(data[0]['name'])
print(data[0]['smiles'])
print(data[1]['smiles'])
for molecule in data:
    print(molecule['smiles'])
    mol=Chem.MolFromSmiles(molecule['smiles'])
    if mol is None:
       print('Invalid Smiles')
       continue
    canonical_smiles=Chem.MolToSmiles(mol, canonical=True)
    print(canonical_smiles)
    inchi=Chem.MolToInchi(mol)
    print(inchi)
    inchikey=Chem.InchiToInchiKey(inchi)
    print(inchikey)
    mw=round(Descriptors.MolWt(mol),3)
    print(molecule['name'],mw)
    formula=rdMolDescriptors.CalcMolFormula(mol)
    print(formula)
    mol_2d=Chem.Mol(mol)
    AllChem.Compute2DCoords(mol_2d)
    filename_png=f'Homework2/2D_images/{molecule["name"]}.png'
    MolToFile(mol_2d,filename_png,size=(600,400))
    filename_mol=f'Homework2/2D_mol/{molecule["name"]}.mol'
    Chem.MolToMolFile(mol_2d,filename_mol)


