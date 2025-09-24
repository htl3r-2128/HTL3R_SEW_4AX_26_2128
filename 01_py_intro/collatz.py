__author__ = "Paul Bauer, HTL3R"
__date__ = "24.09.2025"
__version__ = "1.0"
__license__ = "GNU GPLv3"


def main() -> object:

def collatz(n) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

if __name__ == "__main__":
    main()
