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


# Funktionen
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
