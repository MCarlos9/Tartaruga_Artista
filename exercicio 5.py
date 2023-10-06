"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import random  #Importando a biblioteca random para alterar as cores enquanto o desenho é feito
import turtle

turtle = turtle.Turtle()
turtle.color('red')
colors = ['purple', 'purple', 'blue', 'cyan', 'pink'] #Lista de cores a serem utilizadas pelo Random

turtle.shape('circle') #Formado Turle Alterado

for _ in [1, 2, 3]:
    color = random.choice(colors) #Utilização do comando random para variar as cores do desenho
    turtle.color(color) #Comando para alterar a cor da turtle
    turtle.forward(100)  #Tamanho alterado 100-->200  #Aba do Envelope Reduzida 200-->100, Ficou desproporcional -_-
    turtle.right(120)

turtle.shape('turtle') #Formado Turle Alterado pela 2° Vez
for _ in [1, 2, 3, 4]:
  color = random.choice(colors) #Utilização do comando random para variar as cores do desenho
  turtle.color(color) #Comando para alterar a cor da turtle
  turtle.forward(200)   #Tamanho alterado 100-->200
  turtle.right(90)