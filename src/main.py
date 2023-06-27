import os
import tkinter
import pywhatkit
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def enviar_estudio():
    print("Hola")

def seleccionar_imagen():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png")])

    if archivo is not None:
        imagen = Image.open(archivo)
        imagen = ImageTk.PhotoImage(imagen)
        lbl_imagen = Label(root, image=imagen)
        lbl_imagen.image = imagen
        lbl_imagen.pack()
        path = os.path.abspath(archivo)
        pywhatkit.sendwhats_image("+584123556285", path)

root = Tk()
w = root.winfo_height()
root.geometry("800x600")

phone_number = tkinter.StringVar()

label1 = Label(root, text="Hello world")
label1.pack()

imagen = PhotoImage(file="src/images/prueba.png")
labelImagen = Label(image=imagen, width=100,height=100)
labelImagen.pack()

button_image = Button(text="Seleccionar Imagen", command=seleccionar_imagen)
button_image.pack()

fieldNumber = Entry(root, textvariable=phone_number)
fieldNumber.pack()

button = Button(text="Enviar Estudio", command=enviar_estudio())
button.pack()

root.mainloop()
