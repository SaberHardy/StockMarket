from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox


def Achats():
    root.destroy()
    call(['python', 'Achats.py'])


def Ventes():
    root.destroy()
    call(['python', 'Ventes.py'])


root = Tk()

root.title("Gestion Des Achats")
root.geometry("600x200+400+200")
root.resizable(False, False)
root.configure(background="#808080")

# Add The title
lbl_title = Label(root, borderwidth=3,
                  relief=SUNKEN,
                  text="Stock Market",
                  font=("Sans Sarif", 25),
                  background="#483D8B",
                  foreground="white",
                  )
lbl_title.place(x=0, y=0, width=600)

btn_register = Button(root, text="Achats",
                      font=("Arial", 25),
                      bg="#483D8B",
                      fg="red",
                      command="achat"
                      )
btn_register.place(x=70, y=100, width=200)

btn_register2 = Button(root, text="Ventes",
                       font=("Arial", 25),
                       bg="#483D8B",
                       fg="red",
                       command="ventes"
                       )
btn_register2.place(x=350, y=100, width=200)

root.mainloop()
