nevek = ["Aloe Vera", "Am Erika", "Ameri Katalin", "Ant Rax", "B. Elek", "B. Ödön"]
telefonszam = ["06305554444", "06206717887", "06404889999", "06302455667","06203334451", "06403457897"]

nev = input("Kérek egy nevet: ")
letezik = False

for i in range(len(nevek)):
    if nev == nevek[i]:
        letezik = True
        print(f"{nev} telefonszáma: {telefonszam[i]}")

if letezik == False:
    print("Ilyen név és hozzá tartozó telefonszám nincs a listámban!")
