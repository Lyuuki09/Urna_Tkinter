from tkinter import *
import tkinter as tk

janela1 = tk.Tk()

janela1.title("Primeira janela")
icone = PhotoImage(file="logo.png")
janela1.iconphoto(True, icone)
janela1.config(background="#190329")

joaogaiola_original = PhotoImage(file="logo.png")

label = Label(janela1,
                text="Special effects", 
               font=('Arial', 50, 'italic'), 
                fg = 'black', 
                bg = "red",
                relief=RAISED,
                bd=10,
                padx=20,
                pady=20,
                image=joaogaiola_original,
                compound='top')
#label.place(x=110, y=0)
label.pack()

botao = Button(janela1, text="Clique me!")
botao.pack()


janela1.mainloop()