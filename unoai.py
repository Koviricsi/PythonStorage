import random
import time

#Kártyák neve

kartyak_neve = {
  "p0": "piros nullás", "s0": "sárga nullás", "k0": "kék nullás", "z0": "zöld nullás",
  "p1": "piros egyes", "s1": "sárga egyes", "k1": "kék egyes", "z1": "zöld egyes",
  "p2": "piros kettes", "s2": "sárga kettes", "k2": "kék kettes", "z2": "zöld kettes",
  "p3": "piros hármas", "s3": "sárga hármas", "k3": "kék hármas", "z3": "zöld hármas",
  "p4": "piros négyes", "s4": "sárga négyes", "k4": "kék négyes", "z4": "zöld négyes",
  "p5": "piros ötös", "s5": "sárga ötös", "k5": "kék ötös", "z5": "zöld ötös",
  "p6": "piros hatos", "s6": "sárga hatos", "k6": "kék hatos", "z6": "zöld hatos",
  "p7": "piros hetes", "s7": "sárga hetes", "k7": "kék hetes", "z7": "zöld hetes",
  "p8": "piros nyolcas", "s8": "sárga nyolcas", "k8": "kék nyolcas", "z8": "zöld nyolcas",
  "p9": "piros kilences", "s9": "sárga kilences", "k9": "kék kilences", "z9": "zöld kilences",
  "pt": "piros tiltó", "st": "sárga tiltó", "kt": "kék tiltó", "zt": "zöld tiltó",
  "pf": "piros irányfordító", "sf": "sárga irányfordító", "kf": "kék irányfordító", "zf": "zöld irányfordító",
  "pp2": "piros +2", "sp2": "sárga +2", "kp2": "kék +2", "zp2": "zöld +2"
}

#Kártya azonosítók

kartyak = ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "pt", "pf", "pp2", 
 "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "st", "sf", "sp2",
 "k0", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "kt", "kf", "kp2",
 "z0", "z1", "z2", "z3", "z4", "z5", "z6", "z7", "z8", "z9", "zt", "zf", "zp2"]

#listák/változók

jatekos_kartyak = []
robot_kartyak = []
megjelenitett = []

#Konzol színek

piros = "\033[0;31m"
sarga = "\033[0;33m"
kek = "\033[0;36m"
zold = "\033[0;32m"
alap = "\033[0m"
fekete = "\033[0;30m"
lila = "\033[0;35m"

#Robotok létrehozása, lap kiosztás

print("\033c")

while True:
  try: 
    robotok = int(input("Mennyi robot legyen?\nVálasz (egész szám):"))
    if robotok <= 0:
      print("\033cHibás adat!")
      continue
    break
  except:
    print("\033cHibás adat!")

for i in range(1, 7+1):
    jatekos_kartyak.append(kartyak[random.randint(0, 51)])

for i in range(robotok):
  ideiglenes = []

  for j in range(1, 7+1):
    ideiglenes.append(kartyak[random.randint(0, 51)])

  robot_kartyak.append(ideiglenes)

#Játékos kártyáinak megjelenítése(definíció)

def megjelenites():
  global megjelenitett
  megjelenitett = []
  for i in range(len(jatekos_kartyak)):
    if str(jatekos_kartyak[i]).startswith("p"):
      megjelenitett += [piros + kartyak_neve[jatekos_kartyak[i]].capitalize() + f"{fekete} | "]
    
    if str(jatekos_kartyak[i]).startswith("s"):
      megjelenitett += [sarga + kartyak_neve[jatekos_kartyak[i]].capitalize() + f"{fekete} | "]

    if str(jatekos_kartyak[i]).startswith("k"):
      megjelenitett += [kek + kartyak_neve[jatekos_kartyak[i]].capitalize() + f"{fekete} | "]
    
    if str(jatekos_kartyak[i]).startswith("z"):
      megjelenitett += [zold + kartyak_neve[jatekos_kartyak[i]].capitalize() + f"{fekete} | "]

#Egy bizonyos lap megjelenítése(definíció)

def megjelenites_egy_lap(lap):
  if str(lap).startswith("p"):
    return piros + kartyak_neve[lap].capitalize()
  
  if str(lap).startswith("s"):
    return sarga + kartyak_neve[lap].capitalize()

  if str(lap).startswith("k"):
    return kek + kartyak_neve[lap].capitalize()
  
  if str(lap).startswith("z"):
    return zold + kartyak_neve[lap].capitalize()
  

#Fordító kártyák logikája


jelenlegi = -1
fordito = False

def forditas():
  global jelenlegi
  global fordito
  if fordito == False:
    if jelenlegi == robotok-1:
      jelenlegi = -1
    else:
      jelenlegi += 1
  else:
    if jelenlegi == -1:
      jelenlegi = robotok-1
    else:
      jelenlegi -= 1



#Játékos kártyáinak kiírása megformázva (definíció)
#Játékos kártya letétel

def jatekos_kartyai():
  global utolso_kartya
  global megjelenitett
  global jelenlegi
  global fordito
  if jelenlegi == -1:
    megjelenites()
    print(f"\n{lila}Utoljára letett kártya: {megjelenites_egy_lap(utolso_kartya)}\n{lila}")
    print(f"{lila}A kártyáid:")
    for i in range(len(megjelenitett)):
      print(f"{lila}{i+1}.", megjelenitett[i], end=f"{alap}")
    print(f"{lila}Írja be a \"0\" parancsot új kártya húzásáshoz!\n")

    lap = None
    ideiglenes = None

    while True:
      try: 
        lap = int(input("Melyik kártyád szeretnéd felhasználni?\n"))
        if lap < 0 or lap > len(jatekos_kartyak):
          print("Hibás adat!")
          continue
      except:
        print("Hibás adat!")
        continue

      if lap == 0:
        jatekos_kartyak.append(kartyak[random.randint(0, 51)])
        megjelenites()
        print(f"\033c{lila}Ezt húztad: {megjelenites_egy_lap(jatekos_kartyak[-1])}{lila}\n")
        time.sleep(1)
        forditas()
        return utolso_kartya
      
      ideiglenes = lap
      lap = jatekos_kartyak[lap-1]

      if lap.startswith(utolso_kartya[0]) or lap.endswith(utolso_kartya[-1]):
        jatekos_kartyak.pop(ideiglenes-1)
        print("\033c")
        if lap in ["pf","sf","kf","zf"]:
          if fordito == False:
            fordito = True
          else:
            fordito = False
        forditas()
        return lap
      else:
        print("Ezt a kártyát nem használhatod!")
  else:
    return utolso_kartya


#Robotok logikája (definíció)

def robotok_kartyai(robot_szama):
  global utolso_kartya
  for lap in range(len(robot_kartyak[robot_szama])):
    if str(robot_kartyak[robot_szama][lap]).startswith(utolso_kartya[0]) or str(robot_kartyak[robot_szama][lap]).endswith(utolso_kartya[-1]):
      utolso_kartya = robot_kartyak[robot_szama][lap]
      robot_kartyak[robot_szama].pop(lap)
      return utolso_kartya
  robot_kartyak[robot_szama].append(kartyak[random.randint(0, 51)])
  return utolso_kartya



#Random kezdő kártya sorsolás

utolso_kartya = kartyak[random.randint(0, 51)]
while utolso_kartya in ["pt", "pf", "pp2", "st", "sf", "sp2", "kt", "kf", "kp2", "zt", "zf", "zp2"]:
    utolso_kartya = kartyak[random.randint(0, 51)]

#A játék "motorja"

while True:
  utolso_kartya = jatekos_kartyai()
  if len(jatekos_kartyak) == 0:
      print(f"{sarga}Gratulálok, győztél!")
      exit()

  for i in range(robotok):
    if jelenlegi == i:
      utolso_kartya = robotok_kartyai(i)

      time.sleep(0.0)

      if len(robot_kartyak[i]) == 0:
        print(f"{lila}A(z) {i+1}. robot után az utolsó kártya a {megjelenites_egy_lap(utolso_kartya)}-ra(re){lila} változott meg.")
        print(f"{lila}A(z) {i+1}. robot győzött!")
        exit()
      print(f"{lila}A(z) {i+1}. robot után az utolsó kártya a {megjelenites_egy_lap(utolso_kartya)}-ra(re){lila} változott meg.")

      if utolso_kartya in ["pf","sf","kf","zf"]:
        if fordito == False:
          fordito = True
        else:
          fordito = False
      forditas()