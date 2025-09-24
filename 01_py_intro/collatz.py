"""
In diesem Modul geht es um die bekannte
Collatz-Folge, bzw. die Collatz-Vermutung
"""

__author__ = "Paul Bauer, HTL3R"
__date__ = "24.09.2025"
__version__ = "1.0"
__license__ = "GNU GPLv3"


def main() -> object:
    """
    überprüft die collatz Methode
    >>> collatz(15)
    46

    überprüft die collatz_sequence Methode
    >>> collatz_sequence(15)
    [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(3)
    [3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(16)
    [16, 8, 4, 2, 1]

    überpüft die longest_collatz_sequence Methode
    >>> longest_collatz_sequence(100)
    [97, 119]
    >>> longest_collatz_sequence(20)
    [19, 21]
    >>> longest_collatz_sequence(50)
    [27, 112]
    >>> longest_collatz_sequence(200)
    [171, 125]
    """


def collatz(n) -> int:
    """
    Diese Methode definiert
    den Collatz-Algorithmus
    :param n: int
    :return: int
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz_sequence(number:int) ->list[int]:
    """
    Diese Methode erstellt eine Liste
    mit der Collatz-Folge von number
    :param number: int
    :return: list[int]
    """
    ergListe = [number]
    if number <= 0:
        return []
    else:
        while number != 1:
            number = collatz(number)
            ergListe.append(number)
    return ergListe

def longest_collatz_sequence(n:int) -> list[int]:
    """
    Diese Methode gibt die längste Collatz-Folge
    mit einem Startwert der kleiner n ist
    :param n: list[int]
    :return:
    """
    longest_sequence = len(collatz_sequence(n))
    if n <= 0:
        return []
    else:
        for i in range(0, n, 1):
            if len(collatz_sequence(i)) >= longest_sequence:
                longest_sequence = len(collatz_sequence(i))
                ergList = [i, longest_sequence]
    return ergList


if __name__ == "__main__":
    main()
