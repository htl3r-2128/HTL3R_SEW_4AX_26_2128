"""
In diesem Modul geht es um
verschiedene rekursive Methoden
"""

__author__ = "Paul Bauer, HTL3R"
__date__ = "24.09.2025"
__version__ = "1.0"
__license__ = "GNU GPLv3"

from time import time

def main() -> object:
    """
    überprüft die M Methode
    >>> M(13)
    91
    >>> M(67)
    91
    >>> M(9)
    91
    """
    t0 = time()
    """
    mit t0 vor dem Ausführen der Methode und
    t1 nach dem Ausführen der Methode, messe
    ich die Zeit der Berechnung.
    """
    m_list = []
    for i in range(1, 201):
        m_list.append(M(i))
    print(m_list)

    d_dict = {}
    for i in range(1, 201):
        d_dict[i] = M(i)
    print(d_dict)
    t1 = time()
    print(t1 - t0)
    """
    Bemerkenswert bei dieser Funktion ist, dass 
    das Ergebnis von i=1 bis i=101 91 ist und
    ab i=102 das Ergebnis immer i-10 ist
    """


def M(n) ->int:
    """
    Diese Methode definiert
    die McCarthy-91-Funktion
    :param n: int
    :return: int
    """
    if n <= 100:
        return M(M(n +11))
    else:
        return n - 10

if __name__ == "__main__":
    main()
