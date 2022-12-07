from mysql.connector import Error
from tkinter import messagebox
from tkmacosx import Button as BT
import mysql.connector
from tkinter import ttk
import mysql.connector
from tkinter import *


class Remove(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Delete Student")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()

        a = StringVar()

        def ent():
            if len(a.get()) == 0:
                messagebox.showinfo("Error", 'Please, enter a valid ID to delete')
            else:
                d = messagebox.askyesno("Confirm!", "Are you sure you want to delete the student?")
                if d:
                    try:
                        self.connection = mysql.connector.connect(
                            host='localhost',
                            database='cruddb',
                            user='root',
                            password='')
                        self.cursor = self.connection.cursor()
                        self.cursor.execute("Delete from tbl_student where student_id = %s", [a.get()])
                        self.connection.commit()
                        self.cursor.close()
                        self.connection.close()
                        messagebox.showinfo("Confirm", "Student Deleted Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error", "Something goes wrong")

        Label(self, text="Enter Student ID", bg='gray', font=("Courier new", 15)).place(x=5, y=40)
        Entry(self, textvariable=a, width=20).place(x=210, y=44)
        Button(self, text="Delete", width=15, font=('arial', 10), command=ent).place(x=200, y=90)


Remove().mainloop()
