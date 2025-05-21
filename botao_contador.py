from tkinter import *
import tkinter as tk

count = 0

def contar():
    global count
    count += 1
    numero.config(text=count)

janela = tk.Tk()
janela.geometry("600x600")
janela.config(bg="#1E1524")

contador = Button(text="ME CLIQUE", command=contar, bg="white",)
contador.config(bg="#FF9900")
contador.config(fg="#000000")
contador.config(activebackground="#FFC46C")
contador.config(activeforeground="#ffffff")
contador.config(bd=0, highlightthickness=0)
contador.config(font=("Comic Sans MS", 20, "bold"))
contador.pack()

numero = Label(janela, text=0)
numero.config(font=("monospace", 40))
numero.pack()


janela.mainloop()