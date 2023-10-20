from tkinter import *

teszt = Tk() #Elnevezés, létrehozás
teszt.geometry("500x500") #Méret beállítás
teszt.title("Teszt GUI") #Név beállításű
icon = PhotoImage(file="icon.png")   #->
teszt.iconphoto(True, icon)             #Ikon beállítás

teszt.mainloop()