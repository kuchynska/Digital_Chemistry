import json
import requests
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
sdf_filename="Homework2/workflow_a_results.sdf"
writer=Chem.SDWriter(sdf_filename)
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
    mol_3d=Chem.AddHs(mol)
    embed_result=AllChem.EmbedMolecule(mol_3d)
    if embed_result != 0:
        print("3D generation failed")
        continue
    AllChem.UFFOptimizeMolecule(mol_3d)
    filename_xyz=f'Homework2/3D_xyz/{molecule["name"]}.xyz'
    Chem.MolToXYZFile(mol_3d, filename_xyz)
    url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{molecule["name"]}/cids/JSON'
    response=requests.get(url,timeout=10)
    print(response.status_code)
    pubchem_data=response.json()
    cid= pubchem_data["IdentifierList"]["CID"][0]
    print(molecule["name"], cid)
    property_url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight/JSON'
    property_response=requests.get(property_url,timeout=10)
    property_data=property_response.json()
    print(property_data)
    pubchem_formula = property_data["PropertyTable"]["Properties"][0]["MolecularFormula"]
    print(molecule["name"], pubchem_formula)
    property_url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight/JSON'
    pubchem_mw=property_data["PropertyTable"]["Properties"][0]["MolecularWeight"]
    print(molecule["name"],mw,pubchem_mw)
    mol_3d.SetProp("PubChem_CID", str(cid))
    mol_3d.SetProp("PubChem_Formula", pubchem_formula)
    mol_3d.SetProp("PubChem_MolecularWeight", str(pubchem_mw))
    writer.write(mol_3d)
writer.close()




