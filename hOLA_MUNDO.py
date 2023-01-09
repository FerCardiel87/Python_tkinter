#gui GRAPHICAL USER INTERFACE
#TKINTER TK INTERFACE
#IMPORTAMOS EL MODULO DE TKINTER
import tkinter as tk
#importamos el modulo del tema de tkinter
from tkinter import ttk

#Creamos un objeto usando la clase TK
ventana = tk.Tk()
#modificamos el tamaño de la ventana (píxeles)
ventana.geometry('600x400')
#cambiamos el nombre de la ventana
ventana.title('Fernando_cardiel')
#configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')

#creamos un metodo evento_click
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento_click')
    #creamos un nuevo boton y mostramos
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()

#creamos un boton(widget) , el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)

#utilizar el pack layouit manager para mostrar el boton de la ventana
boton1.pack()
#iniciamos la ventana(esta linea la ejecutamos al final)
#si la ejecutamos anters, no se muesrtran los cambios anteriores
ventana.mainloop()