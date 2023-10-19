print("\033c")
#szotar
a = {
    "abc":"alma",
    "def":"körte"
}

print(a.get("abc"))

a.update({"ghi":"citrom"})

print(a)

a.pop("abc") #popitem az utolsohoz

print(a)

kulcsok = a.keys()

print(kulcsok)

ertekek = a.values()

print(ertekek)

targyak = a.items()

print(targyak)