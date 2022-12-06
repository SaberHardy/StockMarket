from mysql.connector import Error
from tkinter import messagebox
import mysql.connector
from tkinter import *
import tkinter

connection = mysql.connector.connect(host="localhost",
                                     database='cruddb',
                                     user='root',
                                     password=''
                                     )
cursor = connection.cursor()

blue_bg = '#00CFFF'


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Update Student",
                             font=('Courier new', 40),
                             fg='black')
        self.heading.place(x=100, y=0)
        self.id = Label(master, text='Enter ID', font=('Courier new', 10))
        self.id.place(x=0, y=70)
        self.id_entry = Entry(master, font=('Courier new', 10), width=10)
        self.id_entry.place(x=380, y=70)

        # Search Button
        self.search_btn = Button(master, text="Search", width=8, height=0, bg='orange', command=self.search)
        self.search_btn.place(x=500, y=70)

        self.first = Label(master, text="First Name", font=('Courier new', 10, 'bold'))
        self.first.place(x=0, y=120)

        self.last = Label(master, text="Last Name", font=('Courier new', 10, 'bold'))
        self.last.place(x=0, y=170)

        self.gender = Label(master, text="Gender", font=('Courier new', 10, 'bold'))
        self.gender.place(x=0, y=220)

        self.address = Label(master, text="Address", font=('Courier new', 10, 'bold'))
        self.address.place(x=0, y=270)

        self.contact = Label(master, text="Contact", font=('Courier new', 10, 'bold'))
        self.contact.place(x=0, y=320)

        self.course = Label(master, text="Course", font=('Courier new', 10, 'bold'))
        self.course.place(x=0, y=370)

        """Add entries"""
        self.first_entry = Entry(master, width=25, font=('Courier new', 10, 'bold'))
        self.first_entry.place(x=380, y=120)

        self.last_entry = Entry(master, width=25, font=('Courier new', 10, 'bold'))
        self.last_entry.place(x=380, y=170)

        self.gender_entry = Entry(master, width=25, font=('Courier new', 10, 'bold'))
        self.gender_entry.place(x=380, y=220)

        self.address_entry = Entry(master, width=25, font=('Courier new', 10, 'bold'))
        self.address_entry.place(x=380, y=270)

        self.contact_entry = Entry(master, width=25, font=('Courier new', 10, 'bold'))
        self.contact_entry.place(x=380, y=320)

        self.course_entry = Entry(master, width=25, font=('Courier new', 10, 'bold'))
        self.course_entry.place(x=380, y=370)

        """Create Button to add to database"""
        self.add_to_database = Button(master, text='Update Student',
                                      width=27, height=1, bg='green', fg='black',
                                      command=self.update)
        self.add_to_database.place(x=380, y=420)

    def search(self, *args, **kwargs):
        cursor.execute("SELECT * FROM tbl_student WHERE student_id=%s", [self.id_entry.get()])
        results = cursor.fetchall()

        # iterate throw the database
        for result in results:
            self.n1 = result[1]
            self.n2 = result[2]
            self.n3 = result[3]
            self.n4 = result[4]
            self.n5 = result[5]
            self.n6 = result[6]

        connection.commit()

        # insert into entries to update
        self.first_entry.delete(0, END)
        self.first_entry.insert(0, str(self.n1))

        self.last_entry.delete(0, END)
        self.last_entry.insert(0, str(self.n2))

        self.gender_entry.delete(0, END)
        self.gender_entry.insert(0, str(self.n3))

        self.address_entry.delete(0, END)
        self.address_entry.insert(0, str(self.n4))

        self.contact_entry.delete(0, END)
        self.contact_entry.insert(0, str(self.n5))

        self.course_entry.delete(0, END)
        self.course_entry.insert(0, str(self.n6))

    def update(self, *args, **kwargs):
        self.u1 = self.first_entry.get()
        self.u2 = self.last_entry.get()
        self.u3 = self.gender_entry.get()
        self.u4 = self.address_entry.get()
        self.u5 = self.contact_entry.get()
        self.u6 = self.course_entry.get()

        cursor.execute("UPDATE tbl_student SET "
                       "FirstName=%s,"
                       "LastName=%s,"
                       "Gender=%s,"
                       "Address=%s,"
                       "Contact=%s,"
                       "Course=%s WHERE student_id=%s",
                       [self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.id_entry.get()]
                       )

        connection.commit()

        tkinter.messagebox.showinfo("Success", "The student updated successfully!!")


master = Tk()
db = Database(master)
master.title("Update Student")
# root.configure(bg='#00CFFF')
master.geometry("1000x760+0+0")

master.mainloop()
