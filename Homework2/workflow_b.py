import json
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import MolToFile
filename = input("Enter JSON filename: ")

with open(filename) as file:
    data = json.load(file)

print(data["workflow_name"])
scaffold_smiles = data["scaffold"]["smiles"]
scaffold_mol=Chem.MolFromSmiles(scaffold_smiles)
if scaffold_mol is None:
    raise ValueError("Invalid scaffold SMILES")
fragments= data["fragments"]
writer=Chem.SDWriter("Homework2/workflow_b_results.sdf")
for fragment in fragments:
    name = fragment["name"]
    smiles = fragment["smiles"]
    print(name, smiles)
    fragment_mol=Chem.MolFromSmiles(smiles)
    print(name, fragment_mol)
    if fragment_mol is None:
        raise ValueError("Invalid fragment SMILES")
    combined_mol=Chem.CombineMols(scaffold_mol,fragment_mol)
    editable_mol=Chem.RWMol(combined_mol)
    neighbor_indices = []
    dummy_indices = []
    for atom in editable_mol.GetAtoms():
        if atom.GetAtomicNum()==0:
            neighbor_idx=atom.GetNeighbors()[0].GetIdx()
            neighbor_indices.append(neighbor_idx)
            dummy_indices.append(atom.GetIdx())
    print(neighbor_indices)
    editable_mol.AddBond(neighbor_indices[0],neighbor_indices[1],Chem.BondType.SINGLE)
    for idx in sorted(dummy_indices, reverse=True):
        editable_mol.RemoveAtom(idx)
    product_mol=editable_mol.GetMol()
    Chem.SanitizeMol(product_mol)
    product_smiles=Chem.MolToSmiles(product_mol)
    print(name, product_smiles)
    mol_2d = Chem.Mol(product_mol)
    AllChem.Compute2DCoords(mol_2d)
    filename_png=f'Homework2/WorkflowB_2D/{name}.png'
    MolToFile(mol_2d, filename_png, size=(600,400))
    mol_3d=Chem.AddHs(product_mol)
    embed_result = AllChem.EmbedMolecule(mol_3d)
    if embed_result != 0:
        print("3D generation failed")
        continue
    AllChem.UFFOptimizeMolecule(mol_3d)
    filename_xyz = f'Homework2/WorkflowB_3D/{name}.xyz'
    product_mol.SetProp("Fragment", name)
    product_mol.SetProp("SMILES", product_smiles)
    writer.write(product_mol)
    Chem.MolToXYZFile(mol_3d,filename_xyz)
writer.close()

print("Workflow B completed")
print("Total molecules:", len(fragments))
print("SDF file: Homework2/workflow_b_results.sdf")