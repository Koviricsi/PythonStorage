def uj_terminal():
    print("\033c")

def osszeadas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyit szeretnél hozzáadni?\n"))
                szam1 += szam2
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
    uj_terminal()
    return szam1

def kivonas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyit szeretnél kivonni?\n"))
                szam1 -= szam2
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
    uj_terminal()
    return szam1

def szorzas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyivel szeretnél szorozni?\n"))
                szam1 *= szam2
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
    uj_terminal()
    return szam1

def osztas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyivel szeretnél osztani?\n"))
                szam1 /= szam2
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
            except ZeroDivisionError:
                 uj_terminal()
                 print("Hiba! Nullával nem lehet osztani. Próbálja újra!")
    uj_terminal()
    return szam1

def hatvany(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Hányadik hatványra emeljük?\n"))
                szam1 **= szam2
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
    uj_terminal()
    return szam1

def maradek(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyivel szeretne osztani, hogy maradékot kapjon?\n"))
                szam1 %= szam2
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
            except ZeroDivisionError:
                 uj_terminal()
                 print("Hiba! Nullával nem lehet osztani. Próbálja újra!")
    uj_terminal()
    return szam1

menu = True
while True:
            try:
                szam = float(input("Kérlek adj meg egy kezdő számot: \n"))
                uj_terminal()
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
            except OverflowError:
                uj_terminal()
                print("Hiba! Túl nagy szám az összeg. Próbálja újra!")
while True:
    if menu == True:
        menu = False
        print(f"Jelenlegi összeg: {szam}\n\n1 -> Összeadás\n2 -> Kivonás\n3 -> Szorzás\n4 -> Osztás\n5 -> Hatványozás\n6 -> Maradék számítás\n7 -> Törlés (Nullázás)\n8 -> Kilépés\n")
        while True:
            try:
                opcio = int(input("Válasszon az alábbiak közül egy műveletet!\n"))
                break
            except ValueError:
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
        uj_terminal()
    if opcio == 1:
       szam = osszeadas(szam)
    elif opcio == 2:
       szam = kivonas(szam)
    elif opcio == 3:
       szam = szorzas(szam)
    elif opcio == 4:
       szam = osztas(szam)
    elif opcio == 5:
       szam = hatvany(szam)
    elif opcio == 6:
       szam = maradek(szam)
    elif opcio == 7:
       szam = 0
    elif opcio == 8:
        break

    menu = True
    print(f"Jelenlegi összeg: {szam}\n")