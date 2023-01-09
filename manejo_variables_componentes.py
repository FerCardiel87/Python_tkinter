import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

#etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():

#modificamos el txt del label
    etiqueta1.config(text=entrada1.get())
#messagebox (cajas mensajes)
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + 'Informativo')
        messagebox.showerror('Mensaje Error', mensaje1 + 'Error')
        messagebox.showwarning('Mensaje Alerta', mensaje1 + 'Alerta')

#creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)



ventana.mainloop()