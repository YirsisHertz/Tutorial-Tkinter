#-*- coding:utf-8 -*-

from tkinter import *
from tkinter import colorchooser

def abrir_paleta():
    paleta = colorchooser.askcolor()

    r.set(int(paleta[0][0]))
    g.set(int(paleta[0][1]))
    b.set(int(paleta[0][2]))

    hexa.set(paleta[1])

    root.configure(bg = paleta[1])
    etiqueta_red.configure(bg = paleta[1])
    etiqueta_green.configure(bg=paleta[1])
    etiqueta_blue.configure(bg=paleta[1])
    etiqueta_hexa.configure(bg=paleta[1])

if __name__ == "__main__":
    root = Tk()

    root.geometry("300x260")
    root.resizable(0, 0)
    root.title("Paleta De Colores")

    root.call('wm', 'iconphoto', root._w, PhotoImage(file = 'favicon.png'))

    hexa = StringVar()
    r = StringVar()
    g = StringVar()
    b = StringVar()

    etiqueta_red = Label(root, text = "Red:", font = "BOLD", pady = 5)
    etiqueta_red.pack()

    campo_red = Entry(root, justify = CENTER, textvariable = r).pack()

    etiqueta_green = Label(root, text="Green:", font="BOLD", pady=5)
    etiqueta_green.pack()

    campo_green = Entry(root, justify=CENTER, textvariable = g).pack()

    etiqueta_blue = Label(root, text="Blue:", font="BOLD", pady=5)
    etiqueta_blue.pack()

    campo_blue = Entry(root, justify=CENTER, textvariable = b).pack()

    etiqueta_hexa = Label(root, text="", font="BOLD", pady=5, textvariable = hexa)
    etiqueta_hexa.pack()

    btn_seleccionar = Button(root, text = "Seleccionar", bg = "#222", fg = "#fff", activebackground = "#111", activeforeground = "#fff", font = "BOLD", command = abrir_paleta ).pack()

    root.mainloop()