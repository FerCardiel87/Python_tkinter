import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

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

    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + 'Informativo')

def salir():
    ventana.quit()
    ventana.destroy()
    print("salimos....")
    sys.exit()

def crear_menu():
    #configurar el menu principal
    menu_principal = Menu(ventana)
    #tearoff = False poara evitar que se separe el menu de interfaz
    submenu_archivo = Menu(menu_principal, tearoff=0)
    #agregamos una nueva opcion al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    #agregamos un separator
    submenu_archivo.add_separator()
    #agregamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    #agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    #submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    #agregamos una nueva opcion al submenu
    submenu_ayuda.add_command(label='Acerca de')
    #agregsamos al menu principal este nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    #mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)


boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


crear_menu()

ventana.mainloop()