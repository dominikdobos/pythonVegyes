def feladat_1():
    legnagyobb = 0

    for i in range(100, 100000):
        osszeadas = 0
        utolso_szamjegy = len(str(i))
        utolso = int(str(i)[utolso_szamjegy - 1])
        szamjegyek_szama = len(str(i))
        for j in range(szamjegyek_szama - 1):
            osszeadas += int(str(i)[j])
        if utolso > osszeadas:
            legnagyobb = i

    print(legnagyobb)


def feladat_2():
    darab = 0
    szamok = []
    szam = 100
    while not(darab == 20):
        osztok_szama = 0
        for i in range(szam + 1):
            if szam % (i + 1) == 0:
                osztok_szama += 1
        if osztok_szama == 9:
            darab += 1
            if darab > 10:
                szamok.append(szam)
        szam += 1

    for i in range(len(szamok)):
        print(f"{szamok[i]}", end=" ")


def feladat_3():
    szam = 1
    szamsor = []
    while not(len(szamsor) == 15):
        for i in range(len(str(szam))):
            szamjegy = int(str(szam)[i])
            szam = szamjegy

        szamsor.append(szam)
