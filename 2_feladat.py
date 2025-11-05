szam = int(input("Adj meg egy egész számot "))

def fszam(szam):
    if szam == 0:
        print("A megadott szám nulaaa")
    if szam < 0:
        print("A megadot szám negatív")
    elif szam > 0:
        print("A szám pozitív")

fszam(szam)