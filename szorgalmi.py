print("\033c")
valasz = int(input("Szeretné előre látni a megadott szöveget vagy vakon szeretne szavakat begépelni?\n1 - Szeretném előre látni\n2 - Vakon szeretnék gépelni\n"))

print("\033c")

if valasz == 1:
    print("Az X kisváros egy X-al/el teli hely. A(z) X itt mindig X-k, és mindig van X a(z) X-kon/ken. A város központjában egy hatalmas X található, amely mindig lenyűgözi az ide látogató X-kat/ket.\n A városi múzeumban X-k láthatók, amelyek a város X-t mutatják be. A helyi éttermekben pedig X ételeket kóstolhatunk meg, amelyeket a helyi X-k készítenek el.\n")
    print("Az X-ek helyére találjon ki szavakat!\n")
elif valasz == 2:
    print("Találjon ki 12db szót (személy-, helyszín-, étel- vagy tárgyak neve)!\nNe használjon gyűjtőszavakat, számokat, illetve szavaknak a többes számát az értelmes szöveg érdekében!\n")
else:
    print("Hiba! Nem megfelelő számot adott meg.")
    exit()

szo1 = input("1. szó: ")
szo2 = input("2. szó: ")
szo3 = input("3. szó: ")
szo4 = input("4. szó: ")
szo5 = input("5. szó: ")
szo6 = input("6. szó: ")
szo7 = input("7. szó: ")
szo8 = input("8. szó: ")
szo9 = input("9. szó: ")
szo10 = input("10. szó: ")
szo11 = input("11. szó: ")
szo12 = input("12. szó: ")

print("\033c")

print(f"Az {szo1} kisváros egy {szo2}-al/el teli hely. A(z) {szo3} itt mindig {szo4}-k, és mindig van {szo5} a(z) {szo6}-kon/ken. A város központjában egy hatalmas {szo7} található, amely mindig lenyűgözi az ide látogató {szo8}-kat/ket.\n A városi múzeumban {szo9}-k láthatók, amelyek a város {szo10}-t mutatják be. A helyi éttermekben pedig {szo11} ételeket kóstolhatunk meg, amelyeket a helyi {szo12}-k készítenek el.\n")