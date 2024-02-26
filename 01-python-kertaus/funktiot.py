def moikkaa(nimi: str, maara: int = 1):
    print("moro " + nimi + maara * "!")


def plus(a: int, b: int) -> int:
    return a + b


def start():
    asd = plus(2, 3)

    print(type(asd))

    asd = float(asd)
    print(type(asd))

    moikkaa("Jaska")
    moikkaa("Jaska", maara=5)
