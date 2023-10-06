"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()
turtle.pensize(5)
turtle.shape('circle') #Formato Turtle
turtle.width('15') #Largura de Linha

for color in ['red', 'pink', 'blue', 'black']: #Ordem alterada
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

#Segundo Quadrado

for color in ['blue', 'black', 'red', 'pink']: #Ordem alterada
    turtle.color(color)
    turtle.forward(250)
    turtle.forward(100)
    turtle.right(90)