# Bibliotheken importieren
# json: JSON-Dateien lesen
# requests: Daten von PubChem abrufen
# RDKit: Moleküle bearbeiten und Eigenschaften berechnen

import json
import requests
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import MolToFile

# JSON-Datei einlesen
filename=input("Enter filename: ")
print(filename)

# Datei geöffnet und Moleküldaten geladen
with open(filename) as file:
    data=json.load(file)  
print(len(data))

# Name der SDF-Datei erstellt
sdf_filename="Homework2/workflow_a_results.sdf"

# SDF-Writer erstellt SDF-Datei
writer=Chem.SDWriter(sdf_filename)

# Alle Moleküle aus der JSON-Datei nacheinander bearbeitet
for molecule in data:
    print(molecule['smiles'])

    #Smiles in Molekülobjekt umgewandelt
    mol=Chem.MolFromSmiles(molecule['smiles'])
    #Prüfen, ob der SMILES gültig ist
    if mol is None:
       print('Invalid Smiles')
       continue

     # Canonical SMILES erstellen
    # Eine standardisierte SMILES-Darstellung des Moleküls erzeugen
    canonical_smiles=Chem.MolToSmiles(mol, canonical=True)
    print(canonical_smiles)

    # InChI und InChIKey berechnen
    # Zusätzliche chemische Identifikatoren erstellen
    inchi=Chem.MolToInchi(mol)
    print(inchi)
    inchikey=Chem.InchiToInchiKey(inchi)
    print(inchikey)

    # Molekülmasse und Summenformel berechnen
    # Die Molekülmasse wird auf drei Nachkommastellen gerundet
    mw=round(Descriptors.MolWt(mol),3)
    print(molecule['name'],mw)

    # Die Summenformel wird aus der Molekülstruktur berechnet
    formula=rdMolDescriptors.CalcMolFormula(mol)
    print(formula)

    # 2D-Struktur erstellt
    # Eine Kopie des Moleküls erstellt
    mol_2d=Chem.Mol(mol)

     # 2D-Koordinaten der Atome berechnet
    AllChem.Compute2DCoords(mol_2d)

    # Die Struktur als PNG-Bild gespeichert
    filename_png=f'Homework2/2D_images/{molecule["name"]}.png'
    MolToFile(mol_2d,filename_png,size=(600,400))

    # Die Struktur als MOL-Datei gespeichert
    filename_mol=f'Homework2/2D_mol/{molecule["name"]}.mol'
    Chem.MolToMolFile(mol_2d,filename_mol)

    # 3D-Struktur erstellt
    # Wasserstoffatome zum Molekül hinzugefügt
    mol_3d=Chem.AddHs(mol)

    # 3D-Koordinaten berechnet
    embed_result=AllChem.EmbedMolecule(mol_3d)

    # Geprüft ob die 3D-Struktur erfolgreich erstellt wurde
    if embed_result != 0:
        print("3D generation failed")
        continue

    # Die 3D-Geometrie mit dem UFF optimiert
    AllChem.UFFOptimizeMolecule(mol_3d)

    # Die optimierte Struktur als XYZ-Datei gespeichert
    filename_xyz=f'Homework2/3D_xyz/{molecule["name"]}.xyz'
    Chem.MolToXYZFile(mol_3d, filename_xyz)

    # PubChem CID abgerufen
    # Molekül über seinen Namen in der PubChem-Datenbank suchen
    url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{molecule["name"]}/cids/JSON'

     # Anfrage an PubChem gesendet
    response=requests.get(url,timeout=10)

    # Prüfen, ob die Anfrage erfolgreich war
    print(response.status_code)

    # Antwort als JSON gelesen und CID extrahieren
    pubchem_data=response.json()
    cid= pubchem_data["IdentifierList"]["CID"][0]
    print(molecule["name"], cid)

    # Moleküleigenschaften aus PubChem abgerufen
    # Summenformel und Molekülmasse über die CID abfragen
    property_url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight/JSON'

     # Anfrage gesendet und Antwort als JSON gelesen
    property_response=requests.get(property_url,timeout=10)
    property_data=property_response.json()
    print(property_data)

    # Eigenschaften aus der Antwort entnommen
    pubchem_formula = property_data["PropertyTable"]["Properties"][0]["MolecularFormula"]
    print(molecule["name"], pubchem_formula)
    property_url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight/JSON'
    pubchem_mw=property_data["PropertyTable"]["Properties"][0]["MolecularWeight"]
    print(molecule["name"],mw,pubchem_mw)

    # PubChem-Daten als Eigenschaften gespeichert
    mol_3d.SetProp("PubChem_CID", str(cid))
    mol_3d.SetProp("PubChem_Formula", pubchem_formula)
    mol_3d.SetProp("PubChem_MolecularWeight", str(pubchem_mw))
    # Molekül mit seinen Eigenschaften in die SDF-Datei schreiben
    writer.write(mol_3d)
writer.close()




