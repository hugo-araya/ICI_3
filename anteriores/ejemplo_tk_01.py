import tkinter as tk
from tkinter import ttk

def funcion_apreta():
    print("Hola Boton")

def funcion_interaccion():
    boton2.configure(text = preguntar.get())
    etiqueta.configure(foreground = 'red')
    boton3.configure(text = 'Interactuando')

if __name__ == '__main__':
    # Inicializar la ventana
    ventana = tk.Tk()
    ventana.title("Hola ventana")
    ventana.geometry('200x300+400+300')
        # Agregar una etiqueta
    etiqueta = ttk.Label(ventana, text = 'Buenos dias mundo!!!')
    etiqueta.grid(column = 0, row = 0)

    # Agregar un boton
    boton1 = ttk.Button(ventana, text ="Presiona aqui!!!")
    boton1.grid(column = 0, row = 1)

    # Agregar un boton con accion
    boton2 = ttk.Button(ventana, text ="Apreta aqui!!!", command = funcion_apreta)
    boton2.grid(column = 0, row = 2)

    # Agregar caja de texto
    nombre = tk.StringVar()
    preguntar = ttk.Entry(ventana, width = 20, textvariable = nombre)
    preguntar.grid(column = 0, row = 3)

    # Agregar otro boton con accion
    boton3 = ttk.Button(ventana, text ="Interaccion con Widgets", command = funcion_interaccion)
    boton3.grid(column = 0, row = 4)

    # Activar la ventana
    ventana.mainloop()