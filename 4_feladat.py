s1 = str(input("Adj meg egy szót "))
s2 = str(input("Adj meg mégegy szót "))
s3 = str(input("Adj meg mégegy szót "))
szavak = []
# print(s1, s2, s3)

# szavak = [s1, s2, s3]

# def legkisebb_szo():
#     if len(s1)  < len(s2) < len(s3):
#         print(f"A {len(s1)}. a legkisebb szó")
#     elif len(s1)  > len(s2) < len(s3):
#         print(f"A {len(s2)}. a legkisebb szó")
#     elif len(s1)  > len(s2) > len(s3):
#         print(f"A {len(s3)}. a legkisebb szó")
#     else:
#         print("Kettő vagy több szám egyenlő")

# legkisebb_szo()
szavak.append(s1)
szavak.append(s2)
szavak.append(s3)

def kisebb_szo(szavak_listája):
    legrovidebb = len(szavak_listája[0])
    legrovidebb_szo = szavak_listája[0]

    for szo in szavak_listája:
        if len(szo) < legrovidebb:
            legrovidebb = len(szo)
        legrovidebb_szo = szo
    
    print(f"A legrövidebb szó  {legrovidebb_szo} karakterszáma{legrovidebb}")


szok = ('miért', 'kell', 'ennyi', 'szót', 'írni')
kisebb_szo(szok) 