# Homework 2 – RDKit Workflows

## Ziel

In dieser Aufgabe habe ich mit Python und RDKit gearbeitet. Ich habe Moleküle aus JSON-Dateien eingelesen, ihre Eigenschaften berechnet und 2D- und 3D-Strukturen erstellt.

## Workflow A – Moleküle analysieren

1. Zuerst habe ich sieben Moleküle aus `input_workflow_1.json` mit `json.load()` eingelesen.
2. Mit RDKit habe ich Canonical SMILES, InChI, InChIKey, Molekulargewicht und Summenformel berechnet.
3. Danach habe ich 2D-Strukturen erstellt und als PNG- und MOL-Dateien gespeichert.
4. Für die 3D-Strukturen habe ich Wasserstoffatome hinzugefügt, die Koordinaten berechnet und eine UFF-Optimierung durchgeführt. Die Ergebnisse habe ich als XYZ-Dateien gespeichert.
5. Mit `requests` habe ich PubChem-Daten wie CID, Summenformel und Molekulargewicht abgefragt.
6. Zum Schluss habe ich alle sieben Moleküle mit ihren Eigenschaften in einer SDF-Datei gespeichert.

## Workflow B – Neue Moleküle erstellen

1. Zuerst habe ich ein Scaffold und zehn Fragmente aus `input_workflow_2.json` eingelesen.
2. Mit `Chem.CombineMols()` und `Chem.RWMol()` habe ich das Scaffold mit jedem Fragment verbunden.
3. Danach habe ich die Dummy-Atome entfernt, die Moleküle mit `Chem.SanitizeMol()` überprüft und Canonical SMILES erstellt.
4. Für alle zehn Moleküle habe ich 2D-Strukturen als PNG und optimierte 3D-Strukturen als XYZ gespeichert.
5. Anschließend habe ich die Moleküle mit den Eigenschaften `Fragment` und `SMILES` in einer SDF-Datei gespeichert.
6. Mit `Chem.SDMolSupplier()` habe ich überprüft, ob alle zehn Moleküle richtig eingelesen werden können.

## Verwendete Bibliotheken

- `json` – zum Einlesen der JSON-Dateien
- `rdkit` – zur Bearbeitung und Darstellung der Moleküle
- `requests` – für die PubChem-Abfragen

## Fazit

Ich habe gelernt, wie man Moleküle mit RDKit analysiert und neue Moleküle aus einem Scaffold und Fragmenten erstellt. Außerdem habe ich geübt, JSON-Dateien zu lesen, PubChem-Daten abzufragen und Ergebnisse in verschiedenen Dateiformaten zu speichern.