
import os
import re

ordner = input("Ordner: ")

muster = re.compile(r"\s*\d+\s+([A-Za-z]+)\s+(-?[0-9.]+)\s+(-?[0-9.]+)\s+(-?[0-9.]+)")

for name in sorted(os.listdir(ordner)):
    if name.endswith(".out"):

        pfad = os.path.join(ordner, name)

        with open(pfad, "r", encoding="utf-8-sig") as datei:
            zeilen = datei.readlines()

       
        geometrie = []
        letzte_geometrie = []
        lesen = False

        for zeile in zeilen:

            if "Index Symbol" in zeile:
                geometrie = []
                lesen = True
                continue

            if lesen:
                treffer = muster.match(zeile)

                if treffer:
                    geometrie.append(treffer.groups())

                elif geometrie:
                    letzte_geometrie = geometrie
                    lesen = False

        if lesen and geometrie:
            letzte_geometrie = geometrie


        if letzte_geometrie:

            xyz_name = name.replace(".out", ".xyz")
            xyz_pfad = os.path.join(ordner, xyz_name)

            with open(xyz_pfad, "w") as datei:
                datei.write(str(len(letzte_geometrie)) + "\n")
                datei.write(name + "\n")

                for atom in letzte_geometrie:
                    datei.write(" ".join(atom) + "\n")


