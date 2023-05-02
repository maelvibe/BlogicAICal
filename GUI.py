import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from MAIN import Reader

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
    
    with open('fn.txt', "r+") as f:
        f.truncate(0)
        f.write(filename)

with open('fn.txt') as f:
        fn = f.readlines()
print(fn)

# Boton Seleccionar
#btseleccionar = ttk.Button(root,text='Seleccione un Archivo', command=select_file)

btTrans=ttk.Button(root, text='Transformar Archivo', command= lambda : Reader(fn) )

def save():
    files = [('All Files', '*.*'), 
             ('ICS Files', '*.ics'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
  
btguardar = ttk.Button(root, text = 'Guardar ICS', command = lambda : save())



lbl.pack()
#btseleccionar.pack()
btTrans.pack()
btguardar.pack()

# run the application
root.mainloop()

