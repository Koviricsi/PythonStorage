#1. Feladat


paros = []
paratlan = []

for i in range(1, 20+1):
    if i % 2 == 0:
        paros.append(i)
    else:
        paratlan.append(i)

print(f"Páros számok: {paros}\nPáratlan számok: {paratlan}\n")


#2. Feladat


a = int(input("Adja meg az első számot: "))
b = int(input("Adja meg az második számot: "))
c = 0

if a > b:
    a, b = b, a

osszeg = 0

for i in range(a, b+1):
    osszeg += i

print(f"\nAz összeg: {osszeg}")
print(f"\nAz átlag: {osszeg / (b-a+1)}")


#3. Feladat


evszam1 = int(input("\nAdja meg az első évszámot: "))
evszam2 = int(input("\nAdja meg a második évszámot: "))
szokoevek= ""

if evszam1 > evszam2:
    evszam1, evszam2 = evszam2, evszam1

for i in range(evszam1, evszam2+1):
    if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
        szokoevek += str(i) + "; "

if szokoevek == "":
    print("\nNincs szökőév a megadott tartományban.")
else:
    print(f"\nSzökőévek: {szokoevek}")


#4. Feladat

szam = int(input("\nAdjon meg egy pozitív egész számot: "))
osztok = []
i = 1

while i <= szam:
    if szam % i == 0:
        osztok.append(i)
    i += 1
print(f"A(z) {szam} osztói: {osztok}")