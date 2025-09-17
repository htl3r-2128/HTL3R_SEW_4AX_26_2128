"""


"""
__name__: "Paul Bauer"




# ElIf - Beispiel Fussballspiel

 # der Ball hat eine x- und eine y-Koordinate
ball_pos_x = 34
ball_pos_y = -2

# ein Fußballfeld ist etwa 100m x 70m groß und ein Tor ist etwa 7m breit
# das Tor steht in der Mitte der Grundlinie, damit können die Positionen
# der Pfosten berechnet werden
pfos_1_x = 31.5
pfos_2_x = 38.5

# wenn der Ball im Tor ist
if ball_pos_y < 0 and ball_pos_x > pfos_1_x and ball_pos_x < pfos_2_x:
    # bereite einen neuen Anstoß vor
    print("Tor! Anstoß!")
# wenn der Ball sonstwo über die Grundlinie gerollt ist
elif ball_pos_y < 0:
    # dann gibt es auch einen Abstoß
    print("Der Ball ist nicht im Tor! Abstoss!")
# ansonsten
else:
    # der Ball ist im Spielfeld
    print("Der Ball rollt. Er ist rund und das Spiel hat 90 Minuten!")

print("Egal, was passiert: die Fans singen")

# Probier's selbst aus:
# Spiele nun die weiteren 3 Möglichkeiten aus der Abbildung durch,
# wo der Ball sich befinden könnte!


# For-Schleifen
# Aufgabe1:

aufgabe_1_bereich = range(7,19)
for i in aufgabe_1_bereich:
    print(i)

# Aufgabe2:
aufgabe_2_bereich = range(8,19,5)
for i in aufgabe_2_bereich:
    print(i)


"""
Funktionen
"""
# Math - Funktionen

# der Rückgabewert ist die Summe der beiden Argumente (x + y)
def addiere(x, y):
    return x + y

# definiere nun genauso eine Subtraktionsfunktion (x - y)
def subtrahiere(x, y):
    return x - y

# eine Multiplikationsfunktion (x * y)
def multipliziere(x, y):
  return x * y

# eine Quadratfunktion (x * x)
def quadriere(x, y):
  return x ** y

# und eine Minimum-Funktion
# die Minimum-Funktion gibt das Argument zurück, das den kleineren
# Wert hat
def Minimum(x, y):
  if x < y:
    return x
  else:
    return y

# teste alle Funktionen, indem du sie aufrufst und dir die Ergebnisse
# ausgeben lässt

ergebnisAddition = addiere(5, 7)
print("Ergebnis der Addition: " + str(ergebnisAddition))

ergebnisSubtraktion = subtrahiere(5, 7)
print("Ergebnis der Subtraktion: " + str(ergebnisSubtraktion))

ergebnisMultiplikation = multipliziere(3, 6)
print("Ergebnis der Multiplikation: " + str(ergebnisMultiplikation))

ergebnisQuadratfunktion = quadriere(2, 6)
print("Ergebnis der Quadratfunktion: " + str(ergebnisQuadratfunktion))

ergebnisMinimum = Minimum(3, 3)
print("Ergebnis der Minimumfunktion: " + str(ergebnisMinimum))


# Listen

# das Unternehmen hat bereits eine Abrechnungs-Funktion
def abrechnen(auftrag):
    print("Abrechnung erfolgt: " + auftrag)

# initialisiere eine leere Liste für die Aufträge
aufträge = []

# über den Monat: befülle die Liste mit Aufträgen
aufträge.append("auftrag_klaus_schmidt")
aufträge.append("auftrag_hanna_gruber")
aufträge.append("auftrag_michaela_karst")

# Probier's selbst aus:
# Du hast etwas bei dem Unternehmen beauftragt.
# Hänge einen Auftrag mit deinem Namen an die Liste an.
aufträge.append("auftrag_paul_bauer")
#
# am Monatsende: gehe alle Aufträge durch und rechne sie ab
for auftrag in aufträge:
    abrechnen(auftrag)


#Liste Sortieren
# die zu sortierende Liste

unsortierteListe = [2, 5, 7, 9, 1, 3, 6, 4, 8, 0]

# lege eine leere Liste an, in welche die Zahlen einsortiert
# werden sollen
sortierteListe = []

# so lange die unsortierte Liste nicht leer ist
while len(unsortierteListe) != 0:
    # finde das kleinste Element
    kleinsteZahl = min(unsortierteListe)

    # lösche es aus der Liste der unsortierten Zahlen
    unsortierteListe.remove(kleinsteZahl)

    # füge das kleinste Element in die sortierte Liste hinten an
    sortierteListe.append(kleinsteZahl)

# gebe das Ergebnis aus, es sollten die Zahlen 0 bis 9 in aufsteigender
# Reihenfolge angezeigt werden, dann ist dein Algorithmus korrekt
print(sortierteListe)

"""
Dictionaries
"""


# lege ein Dictionary mit Daten einer Kundin an
kunde1 = {
    "vorname": "Sarah",
    "nachname": "Meier",
    "straße": "Goethestraße",
    "hausnummer": 4,
    "telefonnummer": "07315/642735",
    "kontostand": 11.35,
    "istAktivKunde": True
}

# lege noch ein Dictionary mit Daten eines Kunden an
kunde2 = {
    "vorname": "Markus",
    "nachname": "Schreiber",
    "straße": "Lindenstraße",
    "hausnummer": 55,
    "telefonnummer": "03355/392624",
    "kontostand": 4.56,
    "istAktivKunde": False
}

# gebe einige der Werte aus
print(kunde1["vorname"])
print(kunde2["kontostand"])
print(kunde1["telefonnummer"])

# Probier's selbst aus:
# Lass dir den Nachnamen, die Straße und den Kontostand von Markus ausgeben.
print(kunde2["nachname"])
print(kunde2["straße"])
print(kunde2["kontostand"])


# lege zwei Dictionaries an
kunde1 = {
        "vorname": "Sarah",
        "nachname": "Meier",
     }

kunde2 = {
        "vorname": "Markus",
        "nachname": "Schreiber",
     }

# lösche einen Key und den dazugehörigen Wert aus einem Dictionary
del kunde1["vorname"]

# leere das andere Dictionary
kunde2.clear();

# Probier's selbst aus:
# Füge deine Daten im Dictionary "kunde1" hinzu.
# Gebe dann das Dictionary aus.
kunde1["vorname"] = "Paul"
kunde1["nachname"] = "Bauer"

# gebe beide Dictionaries aus
print(kunde1)
print(kunde2)


# Aufgabe: Umgekehrtes Mapping

# gegeben ist ein Dictionary, das pro Kontinent eine Liste verschiedener
# Länder enthält
kontinentZuLänderMapping = {
    "Afrika": ["Kongo", "Sudan", "Südafrika", "Marokko"],
    "Asien": ["Japan", "Indonesien", "Indien", "Bangladesch"],
    "Amerika": ["Kanada", "Brasilien", "Chile", "Uruguay"],
    "Europa": ["Frankreich", "Polen", "Italien", "Slowenien"],
    "Ozeanien": ["Australien", "Neuseeland", "Papua-Neuguinea", "Samoa"]
}

# dieses Mapping soll nun umgekehrt werden, so dass die Daten nach
# folgendem Format vorliegen:
# {
#   "Kongo": "Afrika",
#   "Sudan": "Afrika",
#   ....
#   "Papua-Neuguinea": "Ozeanien",
#   "Samoa": "Ozeanien"
# }
# schreibe das Mapping in dieser Form in dieses Dictionary
länderZuKontinentMapping = {}

# gehe alle Schlüssel (also alle Kontinente) durch
for key in kontinentZuLänderMapping:
    # hole die Liste der Länder von jedem Kontinent
    laenderListe = kontinentZuLänderMapping[key]
    # gehe diese Liste der Länder durch
    for land in laenderListe:
        # schreibe jedes Land als Schlüssel und den dazugehörigen
        # Kontinent als Wert in das Ziel-Dictionary
        länderZuKontinentMapping[land] = key

# diese Funktion gibt ein Dictionary hübsch formatiert auf
# der Konsole aus
def gibDictionaryLesbarAus(d):
    import json
    print(json.dumps(d, sort_keys=False, ensure_ascii=False, indent=4))

# das gegebene und das erstellte Dictionary werden ausgegeben
gibDictionaryLesbarAus(kontinentZuLänderMapping)
gibDictionaryLesbarAus(länderZuKontinentMapping)