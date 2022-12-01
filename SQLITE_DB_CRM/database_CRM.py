import csv
from tkinter import *
from tkinter import ttk
import sqlite3

# Configure DB
# Create or connect to database

conn = sqlite3.connect('tree_crm.db')
# create cursor to database
cursor = conn.cursor()

# Create Table for our database

cursor.execute(
    """
    CREATE TABLE if not exists customers(
    first_name text, 
    last_name text,
    id integer,
    address text,
    city text,
    state text,
    zipcode text)
    """
)

# Add Fake Data
"""
data = [
    ["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
    ["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
    ["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
    ["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
    ["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
    ["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
    ["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
    ["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
    ["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
    ["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
    ["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
    ["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
    ["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
    ["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
    ["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
    ["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
    ["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
    ["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
    ["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
    ["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]

]
"""

# add data to db
'''
for record in data:
    conn.execute("INSERT INTO customers VALUES ("
                 ":first_name,"
                 ":last_name,"
                 ":id,"
                 ":address,"
                 ":city,"
                 ":state,"
                 ":zipcode)",

                 {
                     'first_name': record[0],
                     'last_name': record[1],
                     'id': record[2],
                     'address': record[3],
                     'city': record[4],
                     'state': record[5],
                     'zipcode': record[6],
                 }
                 )
'''
conn.commit()
conn.close()


def query_database():
    conn = sqlite3.connect('tree_crm.db')
    # create cursor to database
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM customers")

    records = cursor.fetchall()
    print(records)
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    conn.commit()
    conn.close()


root = Tk()
root.title('CRM Project TreeBase')
root.geometry("1500x500")

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record".upper())
data_frame.pack(expand=True, anchor=CENTER)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zip code")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)


def clear_entries():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


def select_record(e):
    clear_entries()

    # Grab record number
    selected = my_tree.focus()
    # print(f"SELECTED, {selected}")
    values = my_tree.item(selected, 'values')

    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])


def move_up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


def move_down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


def remove_many():
    x = my_tree.selection()
    for o in x:
        my_tree.delete(o)


def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


def update():
    selected = my_tree.focus()
    # update the record
    my_tree.item(selected, text="", values=(
        fn_entry.get(),
        ln_entry.get(),
        id_entry.get(),
        address_entry.get(),
        city_entry.get(),
        state_entry.get(),
        zipcode_entry.get(),
    ))

    # Update the database
    conn = sqlite3.connect('tree_crm.db')
    # create cursor to database
    cursor = conn.cursor()

    cursor.execute("""
            UPDATE customers SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode 
                
                WHERE oid = :oid""",
                   {
                       'first': fn_entry.get(),
                       'last': ln_entry.get(),
                       'address': address_entry.get(),
                       'city': city_entry.get(),
                       'state': state_entry.get(),
                       'zipcode': zipcode_entry.get(),
                       'oid': id_entry.get()
                   }
                   )

    conn.commit()
    conn.close()

    clear_entries()


# Create Buttons
button_frame = LabelFrame(root, text="Commands".upper())
button_frame.pack(expand=True, anchor=CENTER)

update_button = Button(button_frame, text="Update Record", command=update)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=move_up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=move_down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entries", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# BInd the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database when the program starts
query_database()

root.mainloop()
