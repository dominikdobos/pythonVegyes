import random


def feladat_1():
    print("1. Írd ki, hogy melyik a legnagyobb szám a [100;100000] intervallumból, "
          "amelyiknek az utolsó számjegye nagyobb, mint az előtte lévő számjegyek összege.")

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
    print("2. Írd ki 100-tól kezdve a második 10 darab olyan számot, "
          "amelyiknek pontosan 7 osztója van (1-et és önmagát figyelmen kívül hagyva).")

    darab = 0
    szamok = []
    szam = 100
    while not(darab == 20):
        osztok_szama = 0
        for i in range(2, szam):
            if szam % i == 0:
                osztok_szama += 1
        if osztok_szama == 7:
            darab += 1
            if darab > 10:
                szamok.append(szam)
        szam += 1

    for i in range(len(szamok)):
        print(f"{szamok[i]}", end=" ")
    print()


def feladat_3():
    print("3. Írd ki annak a sorozatnak a 15. elemét, amelyet úgy kapsz meg, "
          "hogy minden következő elemet az előző szám számjegyeinek kétszereséből állítod elő!")

    szamsor = []
    szam = 1
    while not(len(szamsor) == 15):
        str_szam = ""
        for i in range(len(str(szam))):
            jelenlegi_szamjegy = int(str(szam)[i])
            uj_szamjegy = jelenlegi_szamjegy * 2
            str_szam += str(uj_szamjegy)
        szam = int(str_szam)
        szamsor.append(szam)

    print(szamsor[14])


def feladat_4():
    print("4. Sorsolj ki egy 6 számjegyű számot. Add meg, hogy melyik prímszám van ehhez a legközelebb! "
          "Ha több ilyen van, írd ki mindet!")

    szam = random.randint(100000, 999999)
    print(f"A kisorsolt szám: {szam}")
    szam_also = szam - 50
    szam_felso = szam + 50
    primek = []
    for i in range(szam_also, szam_felso):
        for j in range(2, int((i ** 0.5) + 1)):
            if i % j == 0:
                break
        else:
            primek.append(i)

    legkozelebb = []
    legkozelebbi_prim = szam
    legkisebb_kulonbseg = szam
    for i in range(len(primek)):
        if abs(szam - primek[i]) < legkisebb_kulonbseg:
            legkozelebbi_prim = primek[i]
            legkisebb_kulonbseg = abs(szam - primek[i])

    for i in range(len(legkozelebb)):
        if abs(szam - primek[i]) == legkisebb_kulonbseg:
            legkozelebb.append(primek[i])

    print("Legközelebbi prím(ek): ", end="")
    if len(legkozelebb) > 1:
        for i in range(len(legkozelebb)):
            print(legkozelebb[i])
    else:
        print(legkozelebbi_prim)


def feladat_5():
    print("5. Sorsolj ki egy 10 számjegyű számot. Írd ki a számon belüli prímszámokat! "
          "(pl: 1123456789 -> 2, 3, 5, 7, 11, 23, 67, 89, 1123, 4567, 23456789) "
          "A prímszámokat növekvő sorrendben add meg! Ugyanazt a számot ne írd ki kétszer! "
          "Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!")

    szam = random.randint(1000000000, 9999999999)
    prim = []

    for i in range(len(str(szam))):
        str_szam = str(szam)[i]
        if not(str(szam)[i] == "1" or str(szam)[i] == "0"):
            for j in range(2, int((int(str_szam) ** 0.5) + 1)):
                if int(str(szam)[i]) % j == 0:
                    break
            else:
                szerepel_listaban = prim.count(int(str_szam))
                if szerepel_listaban == 0:
                    prim.append(int(str_szam))

        for j in range(i+1, len(str(szam))):
            str_szam += str(szam)[j]
            for g in range(2, int((int(str_szam) ** 0.5) + 1)):
                if int(str_szam) % g == 0:
                    break
            else:
                szerepel_listaban = prim.count(int(str_szam))
                if szerepel_listaban == 0:
                    prim.append(int(str_szam))

    print(f"Kisorsolt szám: {szam}")
    prim.sort()
    for i in range(len(prim)-1):
        print(prim[i], end=", ")
    print(prim[len(prim)-1])


def feladat_6():
    print("6. Sorsolj ki egy 10 számjegyű számot. Melyik az a legnagyobb legalább kétjegyű szám ezen belül, "
          "amelyiknek a számjegyei növekvő sorrendben állnak? (pl: 1234345673 -> 34567) "
          "Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!")

    szam = random.randint(1000000000, 9999999999)
    novekvo_lista = []
    novekvo_szam = ""
    for i in range(len(str(szam))-1):
        if int(str(szam)[i]) < int(str(szam)[i + 1]):
            if len(novekvo_szam) > 0:
                novekvo_szam += str(szam)[i + 1]
                novekvo_lista.append(novekvo_szam)
            else:
                novekvo_szam += str(szam)[i] + str(szam)[i + 1]
                novekvo_lista.append(novekvo_szam)
        else:
            novekvo_szam = ""

    print(f"Kisorsolt szám: {szam}")
    if len(novekvo_lista) > 0:
        legnagyobb = 0
        for i in range(len(novekvo_lista)):
            if int(novekvo_lista[i]) > legnagyobb:
                legnagyobb = int(novekvo_lista[i])

        print(f"Legnagyobb növekvő sorrendben álló szemjegyek a kisorsolt számban: {legnagyobb}")
    else:
        print("Nincs növekvő sorrendben álló szám a kisorsolt számon belül!")
