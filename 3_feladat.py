
def szam_L(szam1, szam2):
    if szam1 > szam2:
        print(f"{szam1} nagyobb mint {szam2}")
    if szam1 < szam2:
        print(f"{szam2} nagyobb mint {szam1}")
    else:
        print("A két szám egyenlő")

szam1 = int(input("Adj meg egy egész számot "))
szam2 = int(input("Adj meg mégegy egész számot "))
szam_L(szam1, szam2)