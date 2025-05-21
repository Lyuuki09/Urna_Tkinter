from operator import itemgetter
from tkinter import *
import tkinter as tk
candidatos = [
    {"nome": "Shaolin Ribeirão Pires", "numero": 10, "partido": "Partido do Futuro", "votos": 0},
    {"nome": "Gabriel Eduardo", "numero": 22, "partido": "União Popular", "votos": 0},
    {"nome": "Carlin Morato", "numero": 33, "partido": "Movimento Nacional", "votos": 0},
    {"nome": "Ana Lima", "numero": 44, "partido": "Poder Democrático", "votos": 0}
]

#votação

janela = tk.Tk()
janela.geometry("1000x700")
janela.config(bg="#24192b")

l1 = Label(janela, text= "Seja bem vindo a Urna Eletrônica!")
l1.config(bg="#24192b", fg="#ffffff", font=("Arial", 20, "bold"))
l1.pack()

l2 = Label(janela, text="O voto é secreto, a democracia é transparente.")
l2.config(bg="#24192b", fg="white", font=("Arial", 11, "italic"))
l2.pack()




pessoas = int(input('Quantas pessoas irão votar?'))
contador = 0
nulo = 0

while contador < pessoas:

    num = int(input('Digite o número do candidato desejado'))
    contador += 1
    voto_valido = False

    for candidato in candidatos:
        for k, v in candidato.items():
            if k == 'numero' and v == num:
                candidato["votos"] += 1
                voto_valido = True
    if voto_valido == False:
        nulo += 1



#Checagem de votos

candidatos.sort(key=itemgetter("votos"), reverse= True)


for chave, valor in enumerate(candidatos):
    print(f'O {chave+1}° lugar foi o {valor["nome"]} com {valor["votos"]} votos')
print(f"Votos nulos: {nulo}")

janela.mainloop()