# Homework 2: RDKit Molecule and Fragment Workflows

## Workflow A: Molecule-Set Workflow

This workflow processes a set of molecules stored in a JSON file using RDKit.

### Input

The input file `molecules.json` contains seven molecules represented by their names and SMILES strings:

- water
- ethanol
- acetone
- acetic acid
- benzene
- aspirin
- caffeine

### Workflow

The Python script `workflow_a.py` performs the following steps:

1. Reads the molecule names and SMILES strings from `molecules.json`.
2. Converts each SMILES string into an RDKit molecule object.
3. Generates molecular identifiers:
   - canonical SMILES
   - InChI
   - InChIKey
4. Saves each molecule as a MOL file.
5. Generates a 2D PNG image for each molecule.
6. Generates a 3D molecular structure using RDKit.
7. Optimizes the 3D geometry using the UFF force field.
8. Saves the optimized structures as XYZ and 3D MOL files.
9. Queries PubChem for molecular information:
   - PubChem CID
   - molecular formula
   - molecular weight
   - XLogP
10. Writes the molecules and PubChem properties into a combined SDF file.

### Output

The generated files are stored in the `output` folder.

For each molecule, the workflow generates:

- `.mol` – molecular structure
- `.png` – 2D structure image
- `.xyz` – optimized 3D coordinates
- `_3d.mol` – optimized 3D molecular structure

The workflow also generates:

- `molecules.sdf` – combined SDF containing the molecules
- `molecules_with_pubchem.sdf` – combined SDF containing molecules and available PubChem properties

### Software

The workflow was implemented in Python using:

- RDKit
- PubChemPy

## Workflow B: Fragment-Library Workflow

This workflow generates a small molecular library by attaching different fragments to a phenyl scaffold.

### Input

The input file `fragments.json` contains a phenyl scaffold and ten fragments:

- methyl
- hydroxyl
- amino
- fluoro
- chloro
- bromo
- cyano
- carboxylic acid
- methoxy
- pyridyl

### Workflow

The Python script `workflow_b.py` performs the following steps:

1. Reads the scaffold and fragments from `fragments.json`.
2. Converts the SMILES strings into RDKit molecule objects.
3. Identifies the dummy atoms used as attachment points.
4. Connects each fragment to the phenyl scaffold.
5. Removes the dummy atoms and generates the resulting molecules.
6. Generates canonical SMILES for the products.
7. Saves each product as a MOL file and a 2D PNG image.
8. Generates 3D structures and optimizes them using the UFF force field.
9. Saves the optimized structures as XYZ and 3D MOL files.
10. Writes all generated molecules into a combined SDF file.
11. Creates a CSV summary containing the molecule names and canonical SMILES.

### Output

The generated files are stored in the `output_b` folder.

For each generated molecule, the workflow creates:

- `.mol` – molecular structure
- `.png` – 2D structure image
- `.xyz` – optimized 3D coordinates
- `_3d.mol` – optimized 3D molecular structure

The workflow also generates:

- `fragment_library.sdf` – combined SDF containing all 10 generated molecules
- `summary.csv` – summary containing molecule names and canonical SMILES