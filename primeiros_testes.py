from tkinter import *
import tkinter as tk

#configurações e criação da janela abaixo

janela1 = tk.Tk() #criando uma janela

janela1.title("Primeira janela") #titulo da janela 
icone = PhotoImage(file="logo.png") # solicitando imagem para inserir futuramente como logo
janela1.iconphoto(True, icone) # modificando o icone da página pela solicitada anteriormente
janela1.config(background="#190329") # mudando a cor do background
joaogaiola_original = PhotoImage(file="logo.png") #criando uma nova imagem para ser utilizada novamente no futuro

#criando uma label (grande inclusive) e suas respectivas configurções
label = Label(janela1, 
                text="Special effects", #texto escrito
               font=('Arial', 50, 'bold'), #fonte
                fg = 'black', #cor do conteúdo principal
                bg = "red", #cor do background
                relief=RAISED, #estilo da borda 
                bd=10, #tamanho da borda
                padx=20, #padding eixo x
                pady=20, #padding eixo y
                image=joaogaiola_original, #imagem a ser selecionada
                compound='top') #configuração para por mais de um elemento principal dentro de uma label
#label.place(x=110, y=0)
label.pack()

#configurações do botão logo abaixo

def clicar():
    print("Dale boy")

botao = Button(janela1, text="Clique me!") # criando o botão 
botao.config(command=clicar) # inserindo a função desejada
botao.config(font=("Ink Free", 30, 'bold')) # definindo a fonte a ser utilizada
botao.config(bg="#054279") # definindo o background do botão
botao.config(fg="#ffffff") # definindo a cor do conteúdo em sí do botão (CSS -> color: "white")
botao.config(activebackground='#FF0000') #definindo a cor do botão após ativado
botao.config(activeforeground='#FFFb1f') #defininfo a cor do conteúdo em sí do botão depois de ativado

# imagem2 = PhotoImage(file="creeper_feioso.png")
# botao.config(image=imagem2) #tranformando o conteúdo do botão em uma imagem
# botao.config(compound='top') #combinando imagem com o texto ou outro elemento dentro do botão

# botao.config(state=DISABLED) #desativa o botão

botao.pack() #posição do botão 

entrada = Entry()
entrada.config(font=("Arial", 30, "bold"), bg="black", fg="white")
entrada.insert(0, "Numero de pessoas na votação")
entrada.pack()



janela1.mainloop()