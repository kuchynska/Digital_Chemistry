import os
import numpy as np
import csv

folder = input("Ordner eingeben: ")

radii = {
    "H": 0.31, "C": 0.76, "N": 0.71,
    "O": 0.66, "F": 0.57, "Si": 1.11,
    "P": 1.07, "S": 1.05, "Cl": 1.02,
    "Ge": 1.20, "As": 1.19, "Se": 1.20,
    "Br": 1.20, "Sn": 1.39, "Te": 1.38,
    "I": 1.39
}

bonds = {}
results = []

# Teil A: Bindungen finden

for filename in os.listdir(folder):
    if filename.endswith(".xyz"):

        path = os.path.join(folder, filename)

        with open(path, "r") as file:
            lines = file.readlines()

        atoms = []
        coords = []

        for line in lines[2:]:
            parts = line.split()

            if len(parts) >= 4:
                atoms.append(parts[0])

                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])

                coords.append([x, y, z])

        coords = np.array(coords)

        for i in range(len(atoms)):
            for j in range(i + 1, len(atoms)):

                a = atoms[i]
                b = atoms[j]

                d = np.linalg.norm(coords[i] - coords[j])
                limit = 1.2 * (radii[a] + radii[b])

                if d <= limit:

                    bond = a + "-" + b
                    reverse = b + "-" + a

                    if reverse in bonds:
                        bond = reverse

                    if bond not in bonds:
                        bonds[bond] = []

                    bonds[bond].append(float(d))

                    results.append([
                        filename, i + 1, j + 1,
                        a, b, bond, round(d, 4)
                    ])

# CSV-Datei für Teil A

with open(os.path.join(folder, "bindungen.csv"), "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Datei", "Atomnummer 1", "Atomnummer 2",
        "Element 1", "Element 2", "Bindungstyp",
        "Bindungslaenge (A)"
    ])

    writer.writerows(results)

# Teil B: Bindungslängen pro Bindungstyp

with open(os.path.join(folder, "bindungslaengen.csv"), "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Bindungstyp", "Anzahl",
        "Minimum (A)", "Maximum (A)", "Mittelwert (A)"
    ])

    for bond in bonds:

        lengths = bonds[bond]

        anzahl = len(lengths)
        minimum = round(np.min(lengths), 4)
        maximum = round(np.max(lengths), 4)
        mittelwert = round(np.mean(lengths), 4)

        writer.writerow([
            bond, anzahl, minimum, maximum, mittelwert
        ])

print("Teil A: bindungen.csv erstellt")
print("Teil B: bindungslaengen.csv erstellt")