"""
In diesem Modul geht es um Palindrome
in verschiedensten Arten.
"""


__author__ = "Paul Bauer, HTL3R"
__date__ = "17.09.2025"
__version__ = "1.2"
__license__ = "GNU GPLv3"

import re


def main() ->object:
    """
    überprüft ob otto ein Palindrom ist
    >>> is_palindrom("Otto")
    True
    >>> is_palindrom("Hans")
    False
    >>> is_palindrom("Anna")
    True

    überprüft die is_palindrom_sentence Methode
    >>> is_palindrom_sentence("Was it a car or a cat I saw?")
    True
    >>> is_palindrom_sentence("Das ist kein Satzpalindrom!")
    False
    >>> is_palindrom_sentence("Trug Tim eine so helle Hose nie mit Gurt?")
    True
    >>> is_palindrom_sentence("Otto ist ein Palindrom!")
    False


    überprüft die palindrom_product Methode
    >>> palindrom_product(910000)
    909909
    >>> palindrom_product(110000)
    109901


    Überprüft die get_dec_hex_palindrom Methode
    >>> get_dec_hex_palindrom(360)
    'Dec: 353, Hex: 161'
    >>> get_dec_hex_palindrom(1)
    'Dec: 1, Hex: 1'
    >>> get_dec_hex_palindrom(20)
    'Dec: 11, Hex: B'
    """


def is_palindrom(s:str) ->bool:
    s = s.lower()
    return s == "".join(reversed(s))

def is_palindrom_sentence(s:str)->bool:
    s = re.sub("[^a-zA-Z0-9]", "", s)
    return is_palindrom(s)

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


def to_base(number:int, base:int)->str:
    """
    to_base rechnet eine Zahl aus dem Dezimalsystem
    in eine Zahl aus einem beliebigen Zahlensystem um.
    Dabei wird die Eingangszahl mit der Basis Modulo gerechnet
    """

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    erg = ""
    while number > 0:
        erg = digits[number % base] + erg
        number //= base
    return erg


def get_dec_hex_palindrom(x)->str:
    """
    Diese Methode geht alle Zahlen ab x nach unten
    durch. Alle Zahlen die sowohl im Dezimalsystem, als
    auch im Hexadezimalsystem ein Palindrom sind werden
    gemeinsam in einem String ausgegeben.
    :param x:
    :return: str
    """
    for i in range (x, 0, -1):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            return "Dec: " + str(i) + ", Hex: " + to_base(i, 16)





if __name__ == "__main__":
    main()
