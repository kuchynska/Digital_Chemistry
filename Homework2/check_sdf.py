from rdkit import Chem
molecules=Chem.SDMolSupplier("Homework2/workflow_b_results.sdf")
print(len(molecules))
for mol in molecules:
    if mol is not None:
        print(mol.GetProp("Fragment"))