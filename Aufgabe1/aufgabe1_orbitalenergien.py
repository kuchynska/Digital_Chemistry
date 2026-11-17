
import os
import csv
import re

ordner = input("Ordner: ")

ergebnisse = []

for name in sorted(os.listdir(ordner)):
    if name.endswith(".out"):

        pfad = os.path.join(ordner, name)

        with open(pfad, "r", encoding="utf-8-sig") as datei:
            text = datei.read()

        homo = re.findall(r"HOMO \(eV\):\s*(-?[0-9.]+)", text)
        lumo = re.findall(r"LUMO \(eV\):\s*(-?[0-9.]+)", text)
        gap = re.findall(r"HOMO-LUMO gap \(eV\):\s*(-?[0-9.]+)", text)

        ergebnisse.append([
            name,
            float(homo[-1]),
            float(lumo[-1]),
            float(gap[-1])
        ])

    with open("Aufgabe1/orbitalenergien.csv", "w", newline="") as datei:
        writer = csv.writer(datei, delimiter=";")

        writer.writerow([
        "Datei",
        "HOMO (eV)",
        "LUMO (eV)",
        "HOMO-LUMO gap (eV)"
    ])

        writer.writerows(ergebnisse)

print("CSV-Datei wurde erstellt!")


groesste = ergebnisse[0]
kleinste = ergebnisse[0]

for zeile in ergebnisse:
    if zeile[3] > groesste[3]:
        groesste = zeile

    if zeile[3] < kleinste[3]:
        kleinste = zeile

print("Groesste Luecke:", groesste[0], groesste[3], "eV")
print("Kleinste Luecke:", kleinste[0], kleinste[3], "eV")
