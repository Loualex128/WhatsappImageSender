import os
import cv2
import pywhatkit
from tkinter import *
from tkinter import filedialog


def seleccionar_imagen():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg ")])

    if archivo is not None:
        path = os.path.abspath(archivo)
        recorte = cv2.imread(path)
        crop_img = recorte[0:910, 25:1120]
        cv2.imwrite(path + "cropped.jpg", crop_img)
        new_path = path + "cropped.jpg"
        #cv2.imshow("cropped", crop_img)
        numero = fieldNumber.get()
        pywhatkit.sendwhats_image(numero, new_path)


root = Tk()
root.title("RX Sender")
w = root.winfo_height()

label = Label(root, text="Ingrese el numero de telefono:")
label.grid(row=0)

button_image = Button(text="Seleccionar imagen y enviar", command=seleccionar_imagen)
button_image.grid(row=2, padx=20, pady=10)

fieldNumber = Entry(root)
fieldNumber.grid(row=1,padx=20, pady=10)

root.mainloop()
