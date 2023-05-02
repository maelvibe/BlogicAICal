import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from MAIN import Caller
import re

# create the root window
root = tk.Tk()
root.title('Agenda BLogic a ICal')
root.resizable(False, False)
root.geometry('300x150')
lbl=tk.Label(root, text= "Convertir Agenda BLogic a ICal")



def select_file():
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Seleccione un Archivo de Agenda de Blogic para cargar',
        initialdir='/',
        filetypes=filetypes)
    
    ARFile = filename.replace("/", "\\")
    print(ARFile)
    
    with open('fn.txt', "r+") as f:
        f.truncate(0)
        f.write(ARFile)

with open('fn.txt') as f:
        fn = f.readlines()

# Boton Seleccionar
btseleccionar = ttk.Button(root,text='Seleccione un Archivo', command=select_file)

btTrans=ttk.Button(root, text='Transformar Archivo', command= lambda : Caller(fn[0]))



lbl.pack()
btseleccionar.pack()
btTrans.pack()

# run the application
root.mainloop()

