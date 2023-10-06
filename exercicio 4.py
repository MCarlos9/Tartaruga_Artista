"""
Exercícios

1) Acrescente ao menos mais duas cores à lista de cores possíveis
Veja os nomes de cores válidos em: https://pt.wikipedia.org/wiki/Lista_de_cores
(coluna Nome Web)
2) Faça o triângulo apontar para cima
3) Remova a cor vermelha da lista de cores possíveis
4) Mude a largura da linha
"""

import turtle
import random

turtle = turtle.Turtle()
colors = ['black', 'purple', 'blue', 'cyan', 'pink']  #Cyan e Pink adicionados ao Random e Red substituido por Black
turtle.width(12) #Largura da linha alterada

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(120)  #Direção Alterada Right-->Left para o triangulo apontar para cima