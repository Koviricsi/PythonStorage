def uj_terminal():
    print("\033c")

def osszeadas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyit szeretnél hozzáadni?\n"))
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
    uj_terminal()
    szam1 += szam2
    return szam1

def kivonas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyit szeretnél kivonni?\n"))
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
    uj_terminal()
    szam1 -= szam2
    return szam1

def szorzas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyivel szeretnél szorozni?\n"))
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
    uj_terminal()
    szam1 *= szam2
    return szam1

def osztas(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyivel szeretnél osztani?\n"))
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
    uj_terminal()
    szam1 /= szam2
    return szam1

def hatvany(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Hányadik hatványra emeljük?\n"))
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
    uj_terminal()
    szam1 **= szam2
    return szam1

def maradek(szam1):
    while True:
            try:
                print("Jelenlegi összeg:", szam1, end="\n")
                szam2 = float(input("Mennyivel szeretne osztani, hogy maradékot kapjon?\n"))
                break
            except ValueError:
                uj_terminal()
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
    uj_terminal()
    szam1 %= szam2
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
while True:
    if menu == True:
        menu = False
        print("1 -> Összeadás\n2 -> Kivonás\n3 -> Szorzás\n4 -> Osztás\n5 -> Hatványozás\n6 -> Maradék számítás\n7 -> Törlés\n8 -> Befejezés\n")
        while True:
            try:
                opcio = int(input("Válasszon az alábbiak közül egy műveletet!\n"))
                break
            except ValueError:
                print("Hiba! Nem érvényes számot adott meg. Próbálja újra!")
        uj_terminal()
    if opcio == 1:
       szam = osszeadas(szam)
       print(f"Jelenlegi összeg: {szam}\n")
       menu = True
    elif opcio == 2:
       szam = kivonas(szam)
       print(f"Jelenlegi összeg: {szam}\n")
       menu = True
    elif opcio == 3:
       szam = szorzas(szam)
       print(f"Jelenlegi összeg: {szam}\n")
       menu = True
    elif opcio == 4:
       szam = osztas(szam)
       print(f"Jelenlegi összeg: {szam}\n")
       menu = True
    elif opcio == 5:
       szam = hatvany(szam)
       print(f"Jelenlegi összeg: {szam}\n")
       menu = True
    elif opcio == 6:
       szam = maradek(szam)
       print(f"Jelenlegi összeg (a maradék): {szam}\n")
       menu = True
    elif opcio == 7:
       szam = 0
       print(f"Jelenlegi összeg: {szam}\n")
       menu = True
    elif opcio == 8:
        break