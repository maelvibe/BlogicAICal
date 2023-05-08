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
    
    global ARFile 
    ARFile = filename.replace("/", "\\")
                                                                                                            

# Boton Seleccionar
btseleccionar = ttk.Button(root,text='Seleccione un Archivo', command=select_file)

btTrans=ttk.Button(root, text='Transformar Archivo', command= lambda : Caller(ARFile))



lbl.pack()
btseleccionar.pack()
btTrans.pack()

# run the application
root.mainloop()

