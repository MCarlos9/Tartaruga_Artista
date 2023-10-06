"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.width(15) #Largura da linha adicionada

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'cyan', 'black', 'orange'] #Cyan,Balck e Orange adicionados a lista
for _ in range (10): #Número de linhas alterado 8-->10
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(35) #Angulo alterado para todas as linhas ficarem visiveis separadamente