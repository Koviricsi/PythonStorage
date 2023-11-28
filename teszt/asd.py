from tkinter import *

print("\033c")

teszt = Tk() #Elnevezés, létrehozás
teszt.geometry("1200x1200") #Méret beállítás
teszt.title("Teszt GUI") #Név beállításű

ikon = PhotoImage(file=r"teszt\icon.png")   #->
teszt.iconphoto(True, ikon)             #Ikon beállítás
teszt.config(background="#45ed88") #Háttér beállítás







szoveg = Label(teszt,
                text="Hello World", #szöveg tartalma
                font=("Arial", 40, "bold"), #szöveg stílus, méret, típus
                fg="#088259",   #betűszín
                relief=RAISED,  #keret
                bd=10,  #keret méret
                padx=20, #padding x
                pady=20, #padding y
                image=ikon, #kép horrárendelése
                compound="bottom", #kép elhelyezése a szöveg mellett
                bg="#96e0c8") #háttérszín
#Szöveg beállítás
szoveg.pack()   #widget elhelyezés (középre felül)
#szoveg.place(x=50,y=50) -> Szöveg elhelyezés bárhol a window-n belül









szamlalo = 0
def klikk():
    global szamlalo
    szamlalo+=1
    print(f"Megnyomtad a gombot {szamlalo} alkalommal")

foto2 = PhotoImage(file=r"teszt\Facebook_Thumb_icon.gif")

gomb = Button(teszt,
                text="Valami", #gomb szöveg
                command=klikk, #függvény meghívása
                font=("Comic Sans", 30, "italic"),
                fg="#088259",
                bg="#96e0c8",
                activeforeground="#0ba874", #betűszín gomb lenyomásakor
                activebackground="#b0e8d6", #háttérszín gomb lenyomásakor
                state=ACTIVE, #gomb állapota (kikapcsolva, bekapcsolva)
                image=foto2,
                compound="bottom"
              )
gomb.pack()













szovegbe = Entry(teszt,
                 font=("Arial", 30),
                 fg="green")  #show="" a karakterek megjelenésének módosításához  #Szöveg bevitel
szovegbe.pack()
szovegbe.insert(0, "Valami") #Alap szöveg, pozíció majd szöveg







def kuld():
    adat = szovegbe.get()
    szovegbe.config(state=DISABLED) #Egy widget config módosítása a futó programban
    print(f"Bevitt szöveg: {adat}")



kuldes = Button(teszt,          #Küldés gomb
                text="küldés",
                font=(50),
                padx=100,
                pady=100,
                command=kuld)
kuldes.pack(side=RIGHT)



def torol():
    szovegbe.delete(0,END)  #0-> első karaktertől a végéig



torles = Button(teszt,          #Törlés gomb
                text="törlés",
                font=(50),
                padx=100,
                pady=100,
                command=torol)
torles.pack(side=RIGHT)



def karaktorol():
    szovegbe.delete(len(szovegbe.get())-1, END) 



karaktertorles = Button(teszt,          #Karakter törlés gomb
                text="karakter törlés",
                font=(50),
                padx=100,
                pady=100,
                command=karaktorol)
karaktertorles.pack(side=RIGHT)





x = IntVar() #vagy StrVar(), 0 vagy 1, false vagy true

def mutat():
    if(x.get() == 1):
        print("ok")
    else:
        print("nem ok")

jelolonegyzet = Checkbutton(teszt,          #Jelölős négyzet
                            text="Valami",
                            font=(30),
                            variable=x, #változó hozzárendelése
                            onvalue=1,  #bejelölt érték
                            offvalue=0, #nem bejelölt érték
                            command=mutat)
jelolonegyzet.pack()









etel = ["pizza", "hamburger", "hotdog"] #tömb
y = IntVar()

def rendeles():
    if(y.get() == 0):
        print("Pizzát rendeltél")
    elif(y.get() == 1):
        print("Hamburgert rendeltél")
    else:
        print("Hotdogot rendeltél")

for i in range(len(etel)):
    radiogomb = Radiobutton(teszt,          #Rádiógombok
                            text=etel[i], #elem választás a tömbből
                            font=(30),
                            width= 10,
                            variable=y,
                            command=rendeles,
                            value=i,    #érték beállítása a gomboknak
                            indicatoron=0)  #karikák kicserélése nyomógombokra
    radiogomb.pack(anchor=W)












mero = Scale(teszt,
             sliderlength=100,
             resolution=10)
mero.pack()





teszt.mainloop()