import tkinter as tk
from tkinter import ttk

def aprete():
    print(ent_entrada.get())

ventana = tk.Tk()
ventana.title('Usando Entry')
ventana.geometry('300x200')
ventana.resizable(0,0)
lbl_etiqueta = ttk.Label(ventana,text="Usuario : ")
lbl_etiqueta.pack()
variable_string = tk.StringVar()
ent_entrada = ttk.Entry(ventana,textvariable=variable_string)
ent_entrada.pack()
boton = ttk.Button(ventana, text = 'Apretar', command=aprete)
boton.pack()
btn_salir = ttk.Button(ventana, text = 'Salir', command=quit)
btn_salir.pack()
ventana.mainloop()