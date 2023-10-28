"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
# °F = (°C x 1,8) + 32

celsius = int(input('Digite a temperatura em Celsius: '))

print(f'{celsius}°C convertido para Fahrenheit ficará {celsius * 1.8 + 32:.2f}°F')