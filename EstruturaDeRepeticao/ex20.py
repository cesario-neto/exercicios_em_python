"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""
numero = int(input('Fatorial de: (min: 1, max: 16)'))
count = int(input('Quantas vezes deseja que o fatorial seja cauculado? '))


resultado = 1
for i in range(1, (numero + 1)):
    resultado *= i
    
novo_resultado = 1

for i in range(count):
    novo_resultado = resultado * novo_resultado
    print(novo_resultado)

