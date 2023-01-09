import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

#width es la cantidad de caracteres que ocupa la caja de texto
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.CENTER)
entrada1.grid(row=0, column=0)

#insert agrega un texto
entrada1.insert(0, 'Introduce una cadena')
entrada1.insert(tk.END, '.')
#entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    #eliminar el contenido
    #entrada1.delete(0, tk.END)
    #seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    #para hacer efectiva la seleccion del texto
    entrada1.focus()

#creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)



ventana.mainloop()