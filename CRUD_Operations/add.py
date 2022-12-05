from mysql.connector import Error
from tkinter import messagebox
from tkmacosx import Button as BT
import mysql.connector
from tkinter import ttk
import mysql.connector
from tkinter import *
import sys
import os

py = sys.executable

blue_bg = '#00CFFF'


class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(600, 600)
        self.minsize(600, 600)
        self.title("Add Student")
        self.canvas = Canvas(width=600, height=600, bg=blue_bg)
        self.canvas.pack()

        first = StringVar()
        last = StringVar()
        gen = StringVar()
        addr = StringVar()
        contact = StringVar()
        cour = StringVar()

        # Check inputs
        def asi():
            try:
                self.connection = mysql.connector.connect(
                    host='localhost',
                    database='cruddb',
                    user='root',
                    password=''
                )

                self.cursor = self.connection.cursor()

                first_name = first.get()
                last_name = last.get()
                gender = gen.get()
                address = addr.get()
                contact_number = contact.get()
                course = cour.get()

                self.cursor.execute(
                    "INSERT INTO tbl_student(FirstName, LastName, Gender, Address, ContactNumber, Course) "
                    "VALUES (%s,%s,%s,%s,%s,%s)",
                    [first_name, last_name, gender, address, contact_number, course])

                self.connection.commit()

                messagebox.showinfo("Done!", "Student Added successfully")

                ask = messagebox.askyesno("Confirm!", "Do you want to add another student?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'add.py'))
                else:
                    self.destroy()
                    self.cursor.close()
                    self.connection.close()
            except Error:
                messagebox.showerror("Error!!", "Something went wrong!")

        Label(self, text='Student Details', bg='gray', fg='white', font=('Courier new', 35, 'bold')).pack()
        Label(self, text='First Name', bg=blue_bg, font=('Courier new', 18, 'bold')).place(x=70, y=102)
        Entry(self, textvariable=first, width=30).place(x=200, y=104)
        Label(self, text='Last Name', bg=blue_bg, font=('Courier new', 18, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=last, width=30).place(x=200, y=152)
        Label(self, text='Gender', bg=blue_bg, font=('Courier new', 18, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=gen, width=30).place(x=200, y=202)
        Label(self, text='Address', bg=blue_bg, font=('Courier new', 18, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=addr, width=30).place(x=200, y=250)
        Label(self, text='Contact', bg=blue_bg, font=('Courier new', 18, 'bold')).place(x=70, y=300)
        Entry(self, textvariable=contact, width=30).place(x=200, y=300)
        Label(self, text='Course', bg=blue_bg, font=('Courier new', 18, 'bold')).place(x=70, y=350)
        Entry(self, textvariable=cour, width=30).place(x=200, y=350)

        BT(self, text="Save", bg="green", width=150, command=asi).place(x=250, y=400)


Add().mainloop()
