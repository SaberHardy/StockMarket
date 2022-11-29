from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
from cProfile import label
import mysql.connector


def Save():
    matricule = txtNumber.get()
    forniseur = txtForniseur.get()
    telephone = txtTelephone.get()
    produit = comboproduit.get()
    prix_achat = txtPrix.get()
    quantite = txtQuantity.get()

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='achat'
    )
    connect = db.cursor()

    try:
        sql = "INSERT INTO tb_achat (code, fourneseur, telephone, produit, prix, quantite) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (matricule, forniseur, telephone, produit, prix_achat, quantite)

        connect.execute(sql, val)
        db.commit()

        dernierMatricule = connect.lastrowid
        messagebox.showinfo("Information", "Achat ajouter")
        root.destroy()

        call(['python', 'Achats.py'])

    except Exception as e:
        print(e)
        db.rollback()
        db.close()


def Edit():
    matricule = txtNumber.get()
    forniseur = txtForniseur.get()
    telephone = txtTelephone.get()
    produit = comboproduit.get()
    prix_achat = txtPrix.get()
    quantite = txtQuantity.get()

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='achat'
    )
    connect = db.cursor()

    try:
        sql = "update tb_achat set fourneseur=%s, telephone=%s, produit=%s, prix=%s, quantite=%s WHERE code=%s"
        val = (forniseur, telephone, produit, prix_achat, quantite, matricule)

        connect.execute(sql, val)
        db.commit()

        dernierMatricule = connect.lastrowid
        messagebox.showinfo("Information", "Achat ajouter")
        root.destroy()

        call(['python', 'Achats.py'])

    except Exception as e:
        print(e)
        db.rollback()
        db.close()


def Return():
    root.destroy()
    call(['python', 'main.py'])


def Delete():
    matricule = txtNumber.get()

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='achat'
    )
    connect = db.cursor()

    try:
        sql = "delete from tb_achat where code=%s"
        val = (matricule,)
        connect.execute(sql, val)
        db.commit()
        dernierMatricule = connect.lastrowid
        messagebox.showinfo("Information", "Achat Supprimer")
        root.destroy()
        call(['python', 'Achats.py'])
    except Exception as e:
        print(e)
        db.rollback()
        db.close()


root = Tk()

root.title("Menu Des Achats")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#808080")

lbl_title = Label(root, borderwidth=3,
                  relief=SUNKEN,
                  text="Gestion Des Achats",
                  font=("Sans Sarif", 25),
                  background="#483D8B",
                  foreground="#FFFAFA")
lbl_title.place(x=0, y=0, width=1350, height=80)

"""Start inputs"""
# Input number ID
lblNumber = Label(root, text="MATRICULE".upper(), font=("Arial", 18), background="#808080", foreground="white")
lblNumber.place(x=70, y=150, width=150)
txtNumber = Entry(root, font=('Arial', 14))
txtNumber.place(x=250, y=150, width=300)

# Forniseur
lblForniseur = Label(root, text="Forniseur".upper(), font=("Arial", 18), background="#808080", fg="white")
lblForniseur.place(x=50, y=200, width=200)
txtForniseur = Entry(root, font=('Arial', 14))
txtForniseur.place(x=250, y=200, width=300)

# Telephone
lblTelephone = Label(root, text="Telephone".upper(), font=("Arial", 18), background="#808080", fg="white")
lblTelephone.place(x=70, y=250, width=150)
txtTelephone = Entry(root, font=('Arial', 14))
txtTelephone.place(x=250, y=250, width=300)

# Achats
lblProduit = Label(root, text="Produit".upper(), font=("Arial", 18), bg="#808080", fg="white")
lblProduit.place(x=550, y=150, width=150)

comboproduit = ttk.Combobox(root, font=("Arial", 15))
comboproduit['values'] = ['IPHONE 11', 'IPHONE 12', 'IPHONE 12 pro max',
                          'GALAXY S2', 'XIAOMI', 'S10',
                          'IPHONE 14 PRO MAX', 'IPHONE 13', 'A10', ]
comboproduit.place(x=700, y=150, width=150)

# Prix
lblPrix = Label(root, text="Prix".upper(), font=("Arial", 18), bg="#808080", fg="white")
lblPrix.place(x=550, y=200, width=150)
txtPrix = Entry(root, font=('Arial', 14))
txtPrix.place(x=700, y=200, width=150)

# Quantity
lblQuantity = Label(root, text="Quantity".upper(), font=("Arial", 18), bg="#808080", fg="white")
lblQuantity.place(x=550, y=250, width=150)
txtQuantity = Entry(root, font=('Arial', 14))
txtQuantity.place(x=700, y=250, width=150)

# add button
add_button = Button(root, text="Save", font=("Arial", 16), bg="#483D8B", fg="black", command=Save)
add_button.place(x=1000, y=140, width=200)

# Edit Button
edit_button = Button(root, text="Edit", font=("Arial", 16), bg="#483D8B", fg="black", command=Edit)
edit_button.place(x=1000, y=190, width=200)

# Delete
edit_button = Button(root, text="Delete", font=("Arial", 16), bg="red", fg="red", command=Delete)
edit_button.place(x=1000, y=240, width=200)

# Return
edit_button = Button(root, text="Return", font=("Arial", 16), bg="white", fg="red", command=Return)
edit_button.place(x=1240, y=240, width=100)

# Create Table

table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), height=10, show='headings')
table.place(x=0, y=290, width=1350, height=700)

table.heading(1, text="Code Achat")
table.heading(2, text="Fourniseur")
table.heading(3, text="Telephone")
table.heading(4, text="Produit")
table.heading(5, text="Prix")
table.heading(6, text="Quantity")

# Columns Dimension
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=50)

# Retrieve from Database
db = mysql.connector.connect(host='localhost', user='root', password='12345', database='achat')
connect = db.cursor()
connect.execute('select * from tb_achat')

for row in connect:
    table.insert('', END, values=row)

db.close()

root.mainloop()
