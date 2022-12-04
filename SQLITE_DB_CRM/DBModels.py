from tkinter import ttk
from tkinter import *
import sqlite3

root = Tk()
root.title('TreeView Tkinter...')
root.geometry("1500x700")

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
tree_scroll.config(command=my_tree.yview)


def query_database():
    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    # for record in records:
    #	print(record)

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

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def search_records():
    lookup_record = search_entry.get()

    search.destroy()
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect('tree_crm.db')
    # create cursor to database
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM customers WHERE last_name like  ?", (lookup_record,))
    records = cursor.fetchall()

    # Add our data to the screen
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


def lookup_records():
    global search_entry, search

    search = Toplevel(root)
    search.title("Search For Client")
    search.geometry("400x200")
    # search.iconbitmap()
    search_frame = LabelFrame(search, text="LAst Name")
    search_frame.pack(padx=10, pady=10)

    search_entry = Entry(search_frame, font=("Arial", 24))
    search_entry.pack(pady=20, padx=20)

    search_button = Button(search, text="Search record", command=search_records)
    search_button.pack(padx=20, pady=20)
