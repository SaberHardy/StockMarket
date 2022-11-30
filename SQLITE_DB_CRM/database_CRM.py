from tkinter import messagebox
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *

root = Tk()
root.title("CRM Actions")
root.geometry("1000x500")

# Add Style
style = ttk.Style()
# Pick a theme
style.theme_use('default')
# Configure the style
style.configure("Treeview",
                background="#D3D3D3",
                foreground='black',
                rowheight=25,
                filedbackground="#D3D3D3")

# Change selected color
style.map('Treeview', background=[('selected', '#343453')])
# Create treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create the treeview
my_tree = ttk.Treeview(tree_scroll, yscrollcommand=tree_scroll.set, selectmode='extended')
my_tree.pack()

# Configure the scroll
tree_scroll.config(command=my_tree.yview)

# Define the columns
my_tree['columns'] = ('First Name', 'Last Name', 'ID', 'City', 'Zip Code', 'State', 'Address')

# Format the columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=140)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zip Code", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zip Code", text="Zip Code", anchor=CENTER)


root.mainloop()
