"""
Exercicios

1) Era para ser um envelope. Mas saiu errado. Corrija.
"""

import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in [1, 2, 3]:
    turtle.forward(100)
    turtle.right(120)

#problema estava na parte abaixo, alterando a ordem do forward e trocando a direção de left-->right já resolve o problema

for _ in [1, 2, 3, 4]:
  turtle.forward(100)
  turtle.right(90)