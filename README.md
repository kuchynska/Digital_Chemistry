# Digital Chemistry – Homework 1

## From Molecular Data to Reaction Network

In this homework, molecular and reaction data were converted from separate CSV tables into structured data.

### Part A – Molecular Records

The files `molecules.csv`, `properties.csv`, and `safety.csv` were combined using the shared `molecule_id`.

The resulting structured molecular records were saved in `molecules.json`. Each molecule contains its identity, properties, and safety information.

### Part B – Reaction Network

The molecular records were combined with the reaction data from `rxn.csv` and `rxn-detail.csv`.

The compounds are represented as nodes and the reactions as directed edges. The reaction network was saved as `rxn-net.json` and visualized in `rxn-net.png`.

### Part C – Query and filtering

Two simple queries were implemented.

The first query finds products that can be reached directly from ethanol. 
The result is:

- Acetaldehyde
- Ethene
- Water

The second query filters reactions with a yield higher than 90%.

The result is:

- R002
- R003

## Reflection

In this homework, molecular data from different CSV files were combined and converted into structured JSON data.

A reaction network was created using NetworkX and visualized with Matplotlib. The network shows the relationships between molecules and the corresponding reaction types.

The exercise also demonstrates how reaction data can be searched and filtered using Python.