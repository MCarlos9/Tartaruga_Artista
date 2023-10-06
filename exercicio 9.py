"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
import random #random importado para melhor execução da troca de cores

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'cyan', 'black'] #Lista de cores a serem utilizadas pelo Random
for c in range(360):
    color = random.choice(colors) #Utilização do comando random para variar as cores do desenho
    turtle.color(color) #Comando para alterar a cor da turtle
    turtle.forward(3) #Diametro do Circulo aumentado
    turtle.right(1)




"turtle.color('red')" #Comando retirado para ser possivel a utilização de cores variadas no desenho