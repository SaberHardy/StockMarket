import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import mysql.connector
from tkmacosx import Button as BT

try:
    connection = mysql.connector.connect(host="localhost",
                                         database='cruddb',
                                         user='root',
                                         password=''
                                         )
    cursor = connection.cursor()

except Exception as err:
    messagebox.showerror('Database Error', 'please, connect your sqlDatabase...')

py = sys.executable
blue_bg = '#00CFFF'
red_bg = 'E60000'


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas(width=1366, height=768, bg=blue_bg)
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320, 768)
        self.state('zoomed')
        self.title('CRUD Operation In Python')

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="#D3D3D3")
        self.style.map('Treeview',
                       background=[('selected', "#347083")])

        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)

        # calling scripts to execute

        def update_fun():
            print(os.system('%s %s' % (py, 'Update.py')))
            os.system('%s %s' % (py, 'Update.py'))

        def delete_fun():
            os.system('%s %s' % (py, 'Delete.py'))

        def add_fun():
            os.system('%s %s' % (py, 'Add.py'))

        columns = ['First Name', 'Last Name', 'Gender',
                   'Address', 'Contact Number', 'Course']
        # Creating Table
        self.listTree = ttk.Treeview(self, height=14, columns=columns)
        self.listTree.tag_configure('oddrow', background="white")
        self.listTree.tag_configure('evenrow', background="lightblue")

        self.verticalScrollbar = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.horizontalScrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.listTree.xview)
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

        self.listTree.place(x=200, y=360)
        self.verticalScrollbar.place(x=1152, y=361, height=374)
        self.horizontalScrollbar.place(x=200, y=720, width=955)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

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

        def check():

            # label and input box
            self.label3 = Label(self, text='CRUD Operations In Python', fg='black', bg=blue_bg,
                                font=('Courier new', 30, 'bold'))
            self.label3.place(x=450, y=100)
            self.label6 = Label(self, text="STUDENT INFORMATION DETAILS", bg=blue_bg,
                                font=('Courier new', 25, 'underline', 'bold'))
            self.label6.place(x=450, y=300)

            self.button = BT(self, text='View Students', width=200, bg='white',
                             font=('Courier new', 20),
                             command=ser)
            self.button.place(x=200, y=250)
            self.button = BT(self, text='Add Student', width=200, bg='green',
                             font=('Courier new', 20),
                             command=add_fun)
            self.button.place(x=470, y=250)
            self.brt = BT(self, text="Update Student", width=200, bg='orange',
                          font=('Courier new', 20),
                          command=update_fun)
            self.brt.place(x=720, y=250)
            self.brt = BT(self, text="Delete Student", width=200, bg='red',
                          font=('Courier new', 20, 'bold'),
                          command=delete_fun)
            self.brt.place(x=980, y=250)

        check()


MainWindow().mainloop()
