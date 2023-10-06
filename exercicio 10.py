"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()

for _ in range(4):
   turtle.color('pink') #Cor adicionada ao Quadrado
   turtle.shape('circle') #Formado da Turtle diferente dos demais
   turtle.forward(100)
   turtle.right(90)


turtle.left(90)
turtle.forward(200)
for _ in range(4):
   turtle.color('black') #Cor adicionada ao Quadrado
   turtle.shape('turtle') #Formado da Turtle diferente dos demais
   turtle.right(90)
   turtle.forward(100)

turtle.left(90) #Linha de codigo adicionado para fazer os quadrados não se tocarem
turtle.forward(100) #Linha de codigo adicionado para fazer os quadrados não se tocarem

for _ in range(4):
   turtle.color('cyan') #Cor adicionada ao Quadrado
   turtle.shape('arrow') #Formado da Turtle diferente dos demais
   turtle.forward(100)
   turtle.left(90)

turtle.left(180) #Linha de codigo adicionado para fazer os quadrados não se tocarem
turtle.right(90) #Linha de codigo adicionado para fazer os quadrados não se tocarem
turtle.forward(300) #Linha de codigo adicionado para fazer os quadrados não se tocarem

for _ in range(4):
   turtle.color('orange') #Cor adicionada ao Quadrado
   turtle.shape('square') #Formado da Turtle diferente dos demais
   turtle.right(90)
   turtle.forward(100)


#Parte adicionada para ser possivel desenhar um quadrado maior ao redor dos demais

turtle.right(90)
turtle.forward(100)
turtle.left(90)
for _ in range(4):
   turtle.color('red') #Cor adicionada ao Quadrado
   turtle.shape('triangle') #Formado da Turtle diferente dos demais
   turtle.left(90)
   turtle.forward(300)