"""
In diesem Modul
"""


__author__ = "Paul Bauer, HTL3R"
__date__ = "17.09.2025"
__version__ = "1.0"
__license__ = "GNU GPLv3"

import re


def main() ->object:
    """
    überprüft ob otto ein Palindrom ist
    >>> is_palindrom("Otto")
    True


    überprüft die is_palindrom_sentence Methode
    >>> is_palindrom_sentence("Was it a car or a cat I saw?")
    True
    >>> is_palindrom_sentence("Das ist kein Satzpalindrom!")
    False

    überprüft die palindrom_product Methode
    >>> palindrom_product(906610)
    906609
    """


def is_palindrom(s:str) ->bool:
    s = s.lower()
    return s == "".join(reversed(s))

def is_palindrom_sentence(s:str)->bool:
    s = re.sub("[^a-zA-Z0-9]", "", s)
    return is_palindrom(s)

def to_base(number:int, base:int)->str:
    """
    to_base rechnet eine Zahl aus dem Dezimalsystem
    in eine Zahl aus einem beliebigen Zahlensystem um.
    Dabei wird die Eingangszahl mit der Basis Modulo gerechnet
    """

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    erg = ""
    while number >= 0:
        erg = digits[number % base] + erg
        number //= base
    return erg




def palindrom_product(x) ->int:
    """
    Diese Methode geht zuerst alle Zahlen ab x
    nach unten durch. Für Jede Zahl wird geschaut,
    ob sie ein Palindrom ist. Falls ja, wird geschaut
    ob sie das Produkt von zwei ganzen dreistelligen Zahlen ist
    :param x:
    :return:int
    """
    for i in range (x,10_000, -1):
        if is_palindrom(str(i)):
            for j in range(100, 1000, +1):
                if (i // j) in range(100, 1000):
                    return i



if __name__ == "__main__":
    main()
