import random
import time

#Konstansok

ALAP = "\033[0m"
TORLES = "\033c"

PIROS = "\033[0;31m"
SARGA = "\033[0;33m"
KEK = "\033[0;36m"
ZOLD = "\033[0;32m"
FEKETE = "\033[0;30m"
LILA = "\033[0;35m"

#Szótárak

kartyak = {
  "p0": f"{PIROS}Piros nullás{ALAP}", "s0": f"{SARGA}Sárga nullás{ALAP}", "k0": f"{KEK}Kék nullás{ALAP}", "z0": f"{ZOLD}Zöld nullás{ALAP}",
  "p1": f"{PIROS}Piros egyes{ALAP}", "s1": f"{SARGA}Sárga egyes{ALAP}", "k1": f"{KEK}Kék egyes{ALAP}", "z1": f"{ZOLD}Zöld egyes{ALAP}",
  "p2": f"{PIROS}Piros kettes{ALAP}", "s2": f"{SARGA}Sárga kettes{ALAP}", "k2": f"{KEK}Kék kettes{ALAP}", "z2": f"{ZOLD}Zöld kettes{ALAP}",
  "p3": f"{PIROS}Piros hármas{ALAP}", "s3": f"{SARGA}Sárga hármas{ALAP}", "k3": f"{KEK}Kék hármas{ALAP}", "z3": f"{ZOLD}Zöld hármas{ALAP}",
  "p4": f"{PIROS}Piros négyes{ALAP}", "s4": f"{SARGA}Sárga négyes{ALAP}", "k4": f"{KEK}Kék négyes{ALAP}", "z4": f"{ZOLD}Zöld négyes{ALAP}",
  "p5": f"{PIROS}Piros ötös{ALAP}", "s5": f"{SARGA}Sárga ötös{ALAP}", "k5": f"{KEK}Kék ötös{ALAP}", "z5": f"{ZOLD}Zöld ötös{ALAP}",
  "p6": f"{PIROS}Piros hatos{ALAP}", "s6": f"{SARGA}Sárga hatos{ALAP}", "k6": f"{KEK}Kék hatos{ALAP}", "z6": f"{ZOLD}Zöld hatos{ALAP}",
  "p7": f"{PIROS}Piros hetes{ALAP}", "s7": f"{SARGA}Sárga hetes{ALAP}", "k7": f"{KEK}Kék hetes{ALAP}", "z7": f"{ZOLD}Zöld hetes{ALAP}",
  "p8": f"{PIROS}Piros nyolcas{ALAP}", "s8": f"{SARGA}Sárga nyolcas{ALAP}", "k8": f"{KEK}Kék nyolcas{ALAP}", "z8": f"{ZOLD}Zöld nyolcas{ALAP}",
  "p9": f"{PIROS}Piros kilences{ALAP}", "s9": f"{SARGA}Sárga kilences{ALAP}", "k9": f"{KEK}Kék kilences{ALAP}", "z9": f"{ZOLD}Zöld kilences{ALAP}",
  "pt": f"{PIROS}Piros tiltó{ALAP}", "st": f"{SARGA}Sárga tiltó{ALAP}", "kt": f"{KEK}Kék tiltó{ALAP}", "zt": f"{ZOLD}Zöld tiltó{ALAP}",
  "pf": f"{PIROS}Piros irányfordító{ALAP}", "sf": f"{SARGA}Sárga irányfordító{ALAP}", "kf": f"{KEK}Kék irányfordító{ALAP}", "zf": f"{ZOLD}Zöld irányfordító{ALAP}",
  "pp2": f"{PIROS}Piros +2{ALAP}", "sp2": f"{SARGA}Sárga +2{ALAP}", "kp2": f"{KEK}Kék +2{ALAP}", "zp2": f"{ZOLD}Zöld +2{ALAP}",
  "bszinvb": f"{PIROS}S{SARGA}z{ZOLD}í{KEK}n{LILA}v{PIROS}á{SARGA}l{ZOLD}a{KEK}s{LILA}z{PIROS}t{SARGA}ó{ALAP}",
  "ap4a" : f"{PIROS}P{SARGA}l{ZOLD}u{KEK}s{LILA}z {PIROS}n{SARGA}é{ZOLD}g{KEK}y{ALAP}"
}

szinek = {"p" : f"{PIROS}(Piros)", "k" : f"{KEK}(Kék)", "z" : f"{ZOLD}(Zöld)", "s" : f"{SARGA}(Sárga)"}

#Listák

jatekos_kartyak = random.choices(list(kartyak.keys()), k=7)
robot_kartyak = []
unok = []

#Változók

robot_mennyiseg = None
sebesseg = None
felso_kartya = None
jelenlegi = -1
fordito = False
plusz_mennyiseg = 1
vege = None

#Definíciók
  
#Jelenlegi játékos meghatározása (fordító (tiltó is!) kártya logikája)

def kovetkezo():
  global jelenlegi, fordito, regi
  regi = jelenlegi
  if fordito == False:
    if jelenlegi == robot_mennyiseg-1:
      jelenlegi = -1
    else:
      jelenlegi += 1
  else:
    if jelenlegi == -1:
      jelenlegi = robot_mennyiseg-1
    else:
      jelenlegi -= 1

#Színválasztás

def szinvalasztas():
  while True:
    try:
      print(f"{TORLES}{PIROS}1. Piros {FEKETE}|{KEK} 2. Kék {FEKETE}|{ZOLD} 3. Zöld {FEKETE}|{SARGA} 4. Sárga{ALAP}")
      szin = int(input(f"{LILA}\nMelyik színre szeretnél váltani?\n"))
      if szin > 4 or szin < 1:
        print("Hibás adat!")
        continue
    except:
      print("Hibás adat!")
    
    if szin == 1:
      return "p"
    elif szin == 2:
      return "k"
    elif szin == 3:
      return "z"
    else:
      return "s"


def jatekos_kezeles():
    global jatekos_kartyak, felso_kartya, plusz_mennyiseg, fordito, szinvalasztas

    uj_lap = ""

#Leteendő kártya bekérés / kártya felhúzás

    if jelenlegi == -1:
        if "ap4a" in felso_kartya or "bszinvb" in felso_kartya:
          szin = felso_kartya[0]
          print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(felso_kartya[1:])} {szinek.get(szin)}\n")
        else:
          print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(felso_kartya)}\n")
        print(f"{LILA}A kártyáid:\n")
        for i in range(len(jatekos_kartyak)):
          print(f"{i+1}. {kartyak.get(jatekos_kartyak[i])}", end=f"{FEKETE} | {ALAP}")
        print(f"{LILA}Írja be a \"0\" parancsot új kártya(k) húzásáshoz!", end=f"\n{ALAP}")

        while True:
            try: 
                lap = int(input(f"{LILA}Melyik kártyádat szeretnéd felhasználni?\n"))
                if lap < 0 or lap > len(jatekos_kartyak):
                    print("Hibás adat!")
                    continue
                uj_lap = jatekos_kartyak[lap-1]
            except:
                print("Hibás adat!")
                continue
            
#Ha a kártya felhúzására kerül sor (játékos oldal)

            if lap == 0:
                if plusz_mennyiseg > 1:
                  print(TORLES)
                  for i in range(plusz_mennyiseg-1):
                    jatekos_kartyak.append(random.choice(list(kartyak.keys())))
                    print(f"{LILA}Ezt húztad: {kartyak.get(jatekos_kartyak[-1])}")
                else:
                  jatekos_kartyak.append(random.choice(list(kartyak.keys())))
                  print(f"{TORLES}{LILA}Ezt húztad: {kartyak.get(jatekos_kartyak[-1])}")

                if "ap4a" in felso_kartya:
                  szin = felso_kartya[0]
                  print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(felso_kartya[1:])} {szinek.get(szin)}\n")
                else:
                  print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(felso_kartya)}\n")
                plusz_mennyiseg = 1
                kovetkezo()
                return felso_kartya
            
#Ha speciális kártya van legfelül (vagy nem lejárt kártya)(játékos oldal)

            elif felso_kartya in ["pp2","sp2","kp2","zp2","pap4a","kap4a","zap4a","sap4a"] and plusz_mennyiseg != 1:
                if uj_lap == "ap4a":
                  jatekos_kartyak.pop(lap-1)
                  plusz_mennyiseg += 4
                  szin = szinvalasztas()
                  print(TORLES + f"\n{LILA}Utoljára letett kártya: {kartyak.get(uj_lap)} {szinek.get(szin)}\n")
                  kovetkezo()
                  return szin + uj_lap
                elif uj_lap in ["pp2","sp2","kp2","zp2"]:
                  jatekos_kartyak.pop(lap-1)
                  plusz_mennyiseg += 2
                  print(TORLES + f"\n{LILA}Utoljára letett kártya: {kartyak.get(uj_lap)}\n")
                  kovetkezo()
                  return uj_lap
                else:
                  print(f"{LILA}A kiválasztott kártyát nem használhatod!\n")
                  continue
            
            else:

#Ha nem speciális kártya van legfelül (vagy lejárt kártya)(játékos oldal)

              if uj_lap.startswith(felso_kartya[0]) or uj_lap.endswith(felso_kartya[-1]) or uj_lap in ["ap4a","bszinvb"]:
                jatekos_kartyak.pop(lap-1)
                print(TORLES)

                if uj_lap in ["pf","sf","kf","zf"]:
                  if fordito == False:
                    fordito = True
                  else:
                    fordito = False

                if uj_lap in ["pt","st","kt","zt"]:
                  print(f"{SARGA}Kitiltottad ebből a körből a", end=" ")
                  kovetkezo()
                  print(f"{jelenlegi+1}. Robotot.")

                if uj_lap == "bszinvb":
                  szin = szinvalasztas()
                  print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(uj_lap)} {szinek.get(szin)}\n")
                  kovetkezo()
                  return szin + uj_lap

                if uj_lap in ["pp2","sp2","kp2","zp2"]:
                  plusz_mennyiseg += 2

                if uj_lap == "ap4a":
                  plusz_mennyiseg += 4
                  szin = szinvalasztas()
                  print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(uj_lap)} {szinek.get(szin)}\n")
                  kovetkezo()
                  return szin + uj_lap
                else:
                  print(f"\n{LILA}Utoljára letett kártya: {kartyak.get(uj_lap)}\n")

                kovetkezo()
                return uj_lap
            
              else:
                print(f"{LILA}A kiválasztott kártyát nem használhatod!\n")
    else:
       return felso_kartya


def robot_kezeles():
  global robot_kartyak, felso_kartya, plusz_mennyiseg, fordito
  for lap in robot_kartyak[jelenlegi]:
     
#Ha speciális kártya van legfelül (vagy nem lejárt kártya)(robot oldal)

     if felso_kartya in ["pp2","sp2","kp2","zp2","pap4a", "kap4a", "zap4a", "sap4a"] and plusz_mennyiseg != 1:
      if lap in ["pp2","sp2","kp2","zp2","ap4a"]:
        if lap == "ap4a":
          robot_kartyak[jelenlegi].pop(robot_kartyak[jelenlegi].index(lap))
          szin = random.choice(list(szinek))
          print(f"{LILA}A(z) {jelenlegi+1}. robot {kartyak.get(lap)} {szinek.get(szin)}{LILA}-t rakott le.{ALAP}\n")
          plusz_mennyiseg += 4
          kovetkezo()
          return szin + lap
        elif lap[0] == felso_kartya[0]:
          print(f"{LILA}A(z) {jelenlegi+1}. robot {kartyak.get(lap)}{LILA}-t rakott le.{ALAP}\n")
          robot_kartyak[jelenlegi].pop(robot_kartyak[jelenlegi].index(lap))
          plusz_mennyiseg += 2
          kovetkezo()
          return lap
        else:
          continue
      else:
        continue
     else:

#Ha nem speciális kártya van legfelül (vagy lejárt kártya)(robot oldal)

      if lap.startswith(felso_kartya[0]) or lap.endswith(felso_kartya[0]) or lap in ["ap4a","bszinvb"]:
          
          robot_kartyak[jelenlegi].pop(robot_kartyak[jelenlegi].index(lap))

          if lap in ["pf","sf","kf","zf"]:
            if fordito == False:
              fordito = True
            else:
              fordito = False

          if lap == "bszinvb":
            szin = random.choice(list(szinek))
            print(f"{LILA}A(z) {jelenlegi+1}. robot {kartyak.get(lap)} {szinek.get(szin)}{LILA}-t rakott le.{ALAP}\n")
            kovetkezo()
            return szin + lap

          if lap in ["pp2","sp2","kp2","zp2"]:
            plusz_mennyiseg += 2

          if lap == "ap4a":
            plusz_mennyiseg += 4
            szin = random.choice(list(szinek))
            print(f"{LILA}A(z) {jelenlegi+1}. robot {kartyak.get(lap)} {szinek.get(szin)}{LILA}-t rakott le.{ALAP}\n")
            kovetkezo()
            return szin + lap

          print(f"{LILA}A(z) {jelenlegi+1}. robot {kartyak.get(lap)}{LILA}-t rakott le.{ALAP}\n")

          if lap in ["pt","st","kt","zt"]:
            print(f"{SARGA}A(z) {jelenlegi+1}. robot kitiltotta ebből a körből a ", end="")
            kovetkezo()
            if jelenlegi != -1:
              print(f"{jelenlegi+1}. Robotot.{ALAP}\n")
            if jelenlegi == -1:
              print(f"játékost!\n{PIROS}Kitiltottak ebből a körből.{ALAP}\n")

          kovetkezo()
          return lap
     
#Ha a robot nem tud lerakni kártyát->
#Ha a kártya felhúzására kerül sor (robot oldal)

#Ha több mint egy kártyát kell felhúzni

  if plusz_mennyiseg > 1:
    for i in range(plusz_mennyiseg-1):
      robot_kartyak[jelenlegi].append(random.choice(list(kartyak.keys())))
    if "ap4a" in felso_kartya:
      szin = felso_kartya[0]
      print(f"{LILA}A(z) {jelenlegi+1}. robot nem tudott lerakni kártyát, ezért felhúzott {PIROS}{plusz_mennyiseg-1} db{LILA} lapot. A felső kártya maradt a(z) {kartyak.get(felso_kartya[1:])} {szinek.get(szin)}{ALAP}\n")
    else:
      print(f"{LILA}A(z) {jelenlegi+1}. robot nem tudott lerakni kártyát, ezért felhúzott {PIROS}{plusz_mennyiseg-1} db{LILA} lapot. A felső kártya maradt a(z) {kartyak.get(felso_kartya)}{ALAP}\n")

#Ha csak egy kártyát kell felhúzni

  else:
    robot_kartyak[jelenlegi].append(random.choice(list(kartyak.keys())))
    if "ap4a" in felso_kartya or "bszinvb" in felso_kartya:
      szin = felso_kartya[0]
      print(f"{LILA}A(z) {jelenlegi+1}. robot nem tudott lerakni kártyát, ezért felhúzott egy lapot. A felső kártya maradt a(z) {kartyak.get(felso_kartya[1:])} {szinek.get(szin)}{ALAP}\n")
    else:
      print(f"{LILA}A(z) {jelenlegi+1}. robot nem tudott lerakni kártyát, ezért felhúzott egy lapot. A felső kártya maradt a(z) {kartyak.get(felso_kartya)}{ALAP}\n")

  plusz_mennyiseg = 1
  kovetkezo()
  return felso_kartya



#Játék előkészítése

print(TORLES)

#Robot szám és sebesség bekérése

while True:
  try: 
    robot_mennyiseg = int(input("Mennyi robot legyen?\nVálasz (egész pozitív szám):"))
    if robot_mennyiseg <= 0:
      print(f"{TORLES}Hibás adat!")
      continue
  except:
    print(f"{TORLES}Hibás adat!")

  try: 
    sebesseg = int(input("Mennyire legyen gyors a játék?\nVálasz (egész pozitív szám, nagyobb szám -> lassabb, min.: 0):"))
    if sebesseg < 0:
      print(f"{TORLES}Hibás adat!")
      continue
    break
  except:
    print(f"{TORLES}Hibás adat!")

#Robotok kártyáinak kisorsolása, "unok" lista beállítása

for i in range(robot_mennyiseg):
  robot_kartyak.append(random.choices(list(kartyak.keys()), k=7))
  unok.append(False)
unok.append(False)

#Kezdő felső kártya kisorsolása

felso_kartya = random.choice(list(kartyak.keys()))
while felso_kartya in ["pt", "pf", "pp2", "st", "sf", "sp2", "kt", "kf", "kp2", "zt", "zf", "zp2", "ap4a", "bszinvb"]:
    felso_kartya = random.choice(list(kartyak.keys()))

#Játék főciklusa
    
print(TORLES)

while True:
#Játékos "motorjának" meghívása 

  felso_kartya = jatekos_kezeles()

#Játékos ellenőrzése (nyert-e, kiálthat-e uno-t)

  if len(jatekos_kartyak) == 0:
    print(TORLES)
    print(f"{SARGA}Gratulálok, nyertél!")
    print(f"{LILA}A robotok maradék kártyái:\n")
    for i in range(len(robot_kartyak)):
      print(f"{i+1}. robot lapjai:", end=" ")
      for j in range(len(robot_kartyak[i])):
        print(kartyak.get(robot_kartyak[i][j]), end=" | ")
      print(LILA)
    break
  elif len(jatekos_kartyak) == 1 and unok[0] == False:
    print(f"{LILA}Játékos mondja: {SARGA}U{ZOLD}N{PIROS}O{KEK}!\n")
    unok[0] = True
  elif len(jatekos_kartyak) > 1:
    unok[0] = False

#Játék sebessége (lassítása)

  time.sleep(sebesseg)

#Robot(ok) "motorjának" meghívása 
  felso_kartya = robot_kezeles()

#Robot ellenőrzése (nyert-e, kiálthat-e uno-t)
  for i in range(robot_mennyiseg):
    if len(robot_kartyak[i]) == 1 and unok[i+1] == False:
      print(f"{LILA}{i+1}. Robot mondja: {SARGA}U{ZOLD}N{PIROS}O{KEK}!\n")
      unok[i+1] = True
    elif len(robot_kartyak[i]) == 0:
      print(f"{PIROS}Vesztettél! A(z) {i+1}. Robot nyert.\n")
      print(ALAP)
      vege = True
      break
    elif len(robot_kartyak[i]) > 1:
      unok[i+1] = False
  if vege:
    break
