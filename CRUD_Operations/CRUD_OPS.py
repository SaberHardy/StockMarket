import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost",
                                         database='cruddb',
                                         user='root',
                                         password=''
                                         )
    cursor = connection.cursor()

except Exception as e:
    print("Something went wrong:", e)

py = sys.executable


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='gray')
        self.canvas = Canvas(width=1400, height=800, bg='gray')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320, 768)
        self.state('zoomed')
        self.title('CRUD Operation In Python')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)

        # calling scripts to execute

        def update_fun():
            os.system('%s %s' % (py, 'Update.py'))

        def delete_fun():
            os.system('%s %s' % (py, 'Delete.py'))

        def add_fun():
            os.system('%s %s' % (py, 'Add.py'))

        # Creating Table
        self.listTree = ttk.Treeview(self, height=14, columns=('First Name', 'Last Name', 'Gender', 'Address',
                                                               'Contact Number', 'Course'))
        self.verticalScrollbar = ttk.Scrollbar(self, orient='vertical', command=self.listTree.yview)
        self.horizontalScrollbar = ttk.Scrollbar(self, orient='horizontal', command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.verticalScrollbar.set, xscrollcommand=self.horizontalScrollbar.set)

        self.listTree.heading("#0", text='ID')
        self.listTree.column('#0', width=50, minwidth=50, anchor='center')

        self.listTree.heading("First Name", text='First Name')
        self.listTree.column('First Name', width=200, minwidth=200, anchor='center')

        self.listTree.heading("Last Name", text='Last Name')
        self.listTree.column('Last Name', width=200, minwidth=200, anchor='center')

        self.listTree.heading("Gender", text='Gender')
        self.listTree.column('Gender', width=125, minwidth=125, anchor='center')

        self.listTree.heading("Address", text='Address')
        self.listTree.column('Address', width=125, minwidth=125, anchor='center')

        self.listTree.heading("Contact Number", text='Contact Number')
        self.listTree.column('Contact Number', width=125, minwidth=125, anchor='center')

        self.listTree.heading("Course", text='Course')
        self.listTree.column('Course', width=125, minwidth=125, anchor='center')

        self.listTree.place(x=200, y=200)
        self.verticalScrollbar.place(x=1150, y=361, height=287)
        self.horizontalScrollbar.place(x=200, y=361, height=966)

        ttk.Style().configure('Treeview', font=('Times new Roman', 15))

        def ser():
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    database='cruddb',
                    user='root',
                    password='')
                cursor = connection.cursor()
                cursor.execute("Select * from tbl_student")
                pc = cursor.fetchall()
                print(f"The pc contains: {pc}")
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("", 'end',
                                             text=row[0],
                                             values=(row[1], row[2], row[3], row[4], row[5], row[6]))

                    else:
                        messagebox.showinfo("Error", "No students to display!!!")
            except Error:
                messagebox.showerror("Error", "Something Goes Wrong!!!")


MainWindow().mainloop()
