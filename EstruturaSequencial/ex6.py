"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
# A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²).
from math import pi


raio = input('Digite o raio do círculo que deseja saber a área: ')
raio = float(raio)
print(f'A área de um círculo cujo raio é de {raio} é exatamente {round(pi * raio ** 2, 2)}')