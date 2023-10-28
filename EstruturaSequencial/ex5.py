"""
Faça um Programa que converta metros para centímetros.
"""

from math import ceil


metros_digitados = input('Digite a quantidade de metros que você dejesa que se transforme em Centímetros: ')
metros_convertido = float(metros_digitados) * 100

print(f'{metros_digitados}m para centímetros é {ceil(metros_convertido)}cm')