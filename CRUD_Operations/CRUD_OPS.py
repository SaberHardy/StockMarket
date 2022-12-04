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



