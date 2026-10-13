# Homework 1: From Molecular Data to Reaction Network

## Part A: CSV-Dateien und JSON

Zuerst habe ich die Datei `molecules.csv` mit Python geöffnet. Dafür habe ich das Modul `csv` und die Funktion `DictReader()` verwendet.

Danach habe ich ein leeres Dictionary erstellt und die Informationen über die Moleküle darin gespeichert. Jedes Molekül hat eine eigene ID (`molecule_id`).

Im nächsten Schritt habe ich die Dateien `properties.csv` und `safety.csv` geöffnet. Mithilfe der `molecule_id` habe ich die Eigenschaften und Sicherheitsinformationen den richtigen Molekülen zugeordnet.

Anschließend habe ich alle Daten mit dem Modul `json` in der Datei `molecules.json` gespeichert.

Am Ende habe ich überprüft, ob die Datei 15 Moleküle enthält und ob die Informationen über Eigenschaften und Sicherheit vorhanden sind.

## Part B: Reaktionsnetzwerk

Zuerst habe ich die Dateien `rxn.csv` und `rxn-detail.csv` mit Python gelesen.

Danach habe ich ein Dictionary für die Reaktionen erstellt. Mithilfe der `reaction_id` habe ich die zusätzlichen Informationen wie Temperatur, Druck und Ausbeute den jeweiligen Reaktionen zugeordnet.

Anschließend habe ich zwei Listen erstellt:

- `nodes` enthält die Moleküle.
- `edges` enthält die Reaktionen zwischen den Molekülen.

Insgesamt habe ich 15 Knoten und 24 Reaktionsdatensätze erstellt.

Danach habe ich die beiden Listen in der Datei `rxn-net.json` gespeichert.

Für die grafische Darstellung habe ich die Bibliotheken `networkx` und `matplotlib` verwendet.

Mit `networkx` habe ich ein gerichtetes Netzwerk erstellt. Die Moleküle werden als Knoten und die Reaktionen als Pfeile dargestellt.

Mit `matplotlib` habe ich das Netzwerk als Bild `rxn-net.png` gespeichert.

## Part C: Suchfunktion

In diesem Teil habe ich eine einfache Funktion namens `find_reactions()` erstellt.

Die Funktion sucht nach Reaktionen eines bestimmten Typs.

Dafür habe ich eine `for`-Funktion verwendet, die alle Reaktionen durchgeht. Mit `if` wird überprüft, ob der Reaktionstyp mit dem gesuchten Typ übereinstimmt.

Zum Beispiel zeigt `find_reactions("oxidation")` die IDs und chemischen Gleichungen aller Oxidationsreaktionen an.

## Part D: Zusammenfassung

Bei dieser Aufgabe habe ich gelernt, wie man CSV-Dateien mit Python liest und Informationen aus mehreren Tabellen miteinander verbindet.

Außerdem habe ich mit Dictionaries, Listen, Schleifen und Funktionen gearbeitet.

Ich habe gelernt, wie man Daten im JSON-Format speichert und ein einfaches Reaktionsnetzwerk erstellt.

Das Netzwerk zeigt, welche Moleküle durch chemische Reaktionen miteinander verbunden sind.