a = int(input("Kérem az első számot: "))
b = int(input("Kérem az második számot: "))
c = int(input("Kérem az harmadik számot: "))

if b < a:
    a = b
if c < a:
    a = c

print(f"A legkisebb szám a {a}")