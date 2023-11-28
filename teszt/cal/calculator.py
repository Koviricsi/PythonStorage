from tkinter import *
import math

window = Tk()
window.geometry("500x750")
window.resizable(False, False)
window.config(bg="grey")
window.title("Asd")
window.iconphoto(True, PhotoImage(file=r"teszt\cal\calicon.png"))

def delete():
    display.delete(0, END)



display = Label(window, font=("Arial", 60), width=90)
display.pack(pady=30, padx=10)

buttons = Canvas(window, bg="grey")
buttons.pack(pady=[70, 0])

row1 = Canvas(buttons, width=500, bg="grey")
row1.pack(side=TOP)

button0 = Button(row1, text="C", font=("Arial", 35, "bold"), width=4)
button1 = Button(row1, text="x^2", font=("Arial", 35, "bold"), width=4)
button2 = Button(row1, text="√2", font=("Arial", 35, "bold"), width=4)
button3 = Button(row1, text="/", font=("Arial", 35, "bold"), width=4)
button0.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

row2 = Canvas(buttons, width=500, bg="grey")
row2.pack(side=TOP)

button0 = Button(row2, text="7", font=("Arial", 35, "bold"), width=4)
button1 = Button(row2, text="8", font=("Arial", 35, "bold"), width=4)
button2 = Button(row2, text="9", font=("Arial", 35, "bold"), width=4)
button3 = Button(row2, text="x", font=("Arial", 35, "bold"), width=4)
button0.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

row3 = Canvas(buttons, width=500, bg="grey")
row3.pack(side=TOP)

button0 = Button(row3, text="4", font=("Arial", 35, "bold"), width=4)
button1 = Button(row3, text="5", font=("Arial", 35, "bold"), width=4)
button2 = Button(row3, text="6", font=("Arial", 35, "bold"), width=4)
button3 = Button(row3, text="-", font=("Arial", 35, "bold"), width=4)
button0.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

row4 = Canvas(buttons, width=500, bg="grey")
row4.pack(side=TOP)

button0 = Button(row4, text="1", font=("Arial", 35, "bold"), width=4)
button1 = Button(row4, text="2", font=("Arial", 35, "bold"), width=4)
button2 = Button(row4, text="3", font=("Arial", 35, "bold"), width=4)
button3 = Button(row4, text="+", font=("Arial", 35, "bold"), width=4)
button0.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

row5 = Canvas(buttons, width=500, bg="grey", border=-2)
row5.pack(side=TOP)

button0 = Button(row5, text="0", font=("Arial", 35, "bold"), width=4)
button1 = Button(row5, text=".", font=("Arial", 35, "bold"), width=4)
button2 = Button(row5, text="+/-", font=("Arial", 35, "bold"), width=4)
button3 = Button(row5, text="=", font=("Arial", 35, "bold"), width=4)
button0.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)


window.mainloop()