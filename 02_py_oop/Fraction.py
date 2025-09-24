__author__ = "Paul Bauer, HTL3R"
__date__ = "24.09.2025"
__version__ = "1.0"
__license__ = "GNU GPLv3"

class Fraction:
    """
    Das ist eine Klasse für
    Bruchzahlen
    """
    def main() -> none:


    def __init__(self, zaehler=0, nenner=0):
        self.zaehler = zaehler
        self.nenner = nenner

    def __str__(self):
        return str(self.zaehler) + "/" + str(self.nenner)

    def __repr__(self):
        return f"Fraction({self.zaehler}, {self.nenner})"

    if __name__ == "__main__":
        main()
