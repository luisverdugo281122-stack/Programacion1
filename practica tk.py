import tkinter as tk
from tkinter import ttk #Themed Tkinter


def saludar():
    etiqueta2.config(text = "Hola, " +entrada_texto.get())

#1. Crear la ventana principal
root = tk.Tk()
root.title("MI primer ventana (Raiz)")
root.geometry("800x600") #WxH Ancho x Alto

#2. Ponemos los widgets
etiqueta = ttk.Label(root, text = "Nombre: ")
etiqueta.grid(row=0, column=0, padx=20, pady=20)

entrada_texto = ttk.Entry(root)
entrada_texto.grid(row=0, column=1, padx=10, pady=20)

etiqueta2 = ttk.Label(root, font="Helvetca 30", background="#0099cc", foreground="#f2f2f2")
etiqueta2.grid(row=1, column=0, columnspan=2)

boton = ttk.Button(root,
text = "Esto es un boton",padding=10)
#boton.grid(row=2, column=0,columnspan=2, padx=20, pady=20)
#boton.pack(pady=20)
boton.place(x=100, y=200)

check = ttk.Checkbutton(
    root,
    text="aceptas los terminos??"
)
check.grid(row=3,colum=0,coumspa=2)

r1= ttk.Radiobutton(root,text="rojo")
r2= ttk.Radiobutton(root,text="verde")
r3= ttk.Radiobutton(root,text="azul")

#3.Siempre va al final
root.mainloop() #Mantiene activa la ventana y escuchando eventos