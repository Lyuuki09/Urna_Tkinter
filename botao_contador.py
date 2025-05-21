from tkinter import *
import tkinter as tk

count = 0

def contar():
    global count
    count += 1
    print(count)

janela = tk.Tk()
janela.geometry("600x600")
janela.config(bg="#1E1524")

contador = Button(text="ME CLIQUE",
                  command=contar,
                  bg="white",
                  )
contador.pack()

janela.mainloop()