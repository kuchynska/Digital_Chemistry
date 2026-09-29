# Digital Chemistry – Homework 1

## From Molecular Data to Reaction Network

In this homework, molecular and reaction data were converted from separate CSV tables into structured data.

### Part A – Molecular Records

The files `molecules.csv`, `properties.csv`, and `safety.csv` were combined using the shared `molecule_id`.

The resulting structured molecular records were saved in `molecules.json`. Each molecule contains its identity, properties, and safety information.

### Part B – Reaction Network

The molecular records were combined with the reaction data from `rxn.csv` and `rxn-detail.csv`.

The compounds are represented as nodes and the reactions as directed edges. The reaction network was saved as `rxn-net.json` and visualized in `rxn-net.png`.

### Part C – Query

A simple query was implemented to find products that can be reached directly from ethanol.

For the current reaction network, the query returns:

`Acetaldehyde`

This shows how structured chemical data can be searched and reused programmatically.