text = input("Írj be egy szöveget:")

text.capitalize()   #mondat első betűje nagybetűs
text.casefold() #karakterlánc kisbetűs legyen
text.lower()    #karakterlánc kisbetűs legyen
text.swapcase() #kisbetűket nagybetűssé, a nagybetűket pedig kisbetűsség

text.title()    #minden szó első betűje nagybetűs

text.upper()    #karakterlánc nagybetűs legyen

print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())




print(chr(98))
print(ord("b"))

print(chr(72))
print(chr(121))
print(chr(223))
print(chr(687))
print(ord("B"))
print(ord("b"))


text = "ez egy python gyakorlás"


text.count("o") #mágszámolja hány "o van a karakterláncban"

text.find("o")  #megmondja az első "o" helyét/indexét
text.index("o") #megmondja az első "o" helyét/indexét

text.rfind("o") #megmondja az utolsó "o" helyét/indexét
text.rindex("o")    #megmondja az utolsó "o" helyét/indexét

text.startswith("o")    #ellenőrzi, hogy "o"-val kezdődik-e
text.endswith("o")  #ellenőrzi, hogy "o"-val végződik-e

len(text)  #karakterlánc hosszát adja meg



print(text.count("p"))
print(text.index("p"))
print(text.rindex("o"))

print(text[4:10])
print(text[:2])
print(text[11:])
print(text[len(text)-1])
print(text[-1])
print(text[0])

text.isnumeric()    #A string számokból áll-e
text.isalpha()    #A string az ábc betűiből áll-e
text.islower()    #A string csak kisbetűkből áll-e
text.isupper()    #A string csak nagybetűkből áll-e

x = input("Adj meg egy egész számot:")
print(f"Számot adtál meg?\n {x.isnumeric()}")
if x.isnumeric() == True:
    print(f"A(z) {x} egy szám")
else:
    print("Nem egész számot adtál meg")


y = input("Írj ide egy szöveget (csak betűkből álljon):\n")

if y.isalpha() == True:
    print("Csak az ábc betűi szerepelnek a beírt szövegben!")
else:
    print("A beírt szöveg nem csak az ábc betűit tartalmazza")

if y.isalpha() == True:
    if y.islower() == True:
        print("A megadott szöveg csupa kisbetűs")
    if y.isupper() == True:
        print("A megadott szöveg csupa nagybetűs")
    else:
        print("A megadott szöveg tartalmaz kis és nagybetűket is")
else:
    print("A beírt szöveg nem csak az ábc betűit tartalmazza")