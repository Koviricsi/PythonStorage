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
    break
  except:
    print("Hibás adat!")

for i in range(1, 7+1):
    jatekos_kartyak.append(kartyak[random.randint(0, 51)])

for i in range(robotok):
  ideiglenes = []

  for j in range(1, 7+1):
    ideiglenes.append(kartyak[random.randint(0, 51)])

  robot_kartyak.append(ideiglenes)

#Játékos kártyáinak kiírása megformázva (definíció)
#Játékos kártya letétel

def jatekos_kartyai(utolso_lap):
  global megjelenitett
  megjelenites()
  print(f"\n{lila}{kartyak_neve[utolso_lap].upper()}\n")
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
        continue
    except:
      print("Hibás adat!")

    if lap == 0:
      jatekos_kartyak.append(kartyak[random.randint(0, 51)])
      megjelenites()
      print("Ezt húztad: "+megjelenitett[-1]+f"{lila}")
      return utolso_lap
    
    ideiglenes = lap
    lap = jatekos_kartyak[lap-1]

    if lap.startswith(utolso_lap[0]) or lap.endswith(utolso_lap[-1]):
      jatekos_kartyak.pop(ideiglenes-1)
      return lap
    else:
      print("Ezt a kártyát nem használhatod!")

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


def robotok_kartyai(robot_szama, utolso_lap):
  for lap in range(len(robot_kartyak[robot_szama])):
    if str(robot_kartyak[robot_szama][lap]).startswith(utolso_lap[0]) or str(robot_kartyak[robot_szama][lap]).endswith(utolso_lap[-1]):
      utolso_lap = robot_kartyak[robot_szama][lap]
      robot_kartyak[robot_szama].pop(lap)
      return utolso_lap
  robot_kartyak[robot_szama].append(kartyak[random.randint(0, 51)])
  return utolso_lap


utolso_kartya = kartyak[random.randint(0, 51)]
while utolso_kartya in ["pt", "pf", "pp2", "st", "sf", "sp2", "kt", "kf", "kp2", "zt", "zf", "zp2"]:
    utolso_kartya = kartyak[random.randint(0, 51)]


while True:
  utolso_kartya = jatekos_kartyai(utolso_kartya)
  if len(jatekos_kartyak) == 0:
      print(f"Gratulálok, győztél!")
      exit()
  for i in range(robotok):
    utolso_kartya = robotok_kartyai(i, utolso_kartya)
    time.sleep(0.4)
    if len(robot_kartyak[i]) == 0:
      print(f"A(z) {i}. robot után az utolsó kártya a {utolso_kartya}-ra(re) változott meg.")
      print(f"A(z) {i}. robot győzött!")
      exit()
    print(f"A(z) {i}. robot után az utolsó kártya a {utolso_kartya}-ra(re) változott meg.")