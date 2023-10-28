"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

# base = input('Digite um número: ')
# expoente = input('Digite o expoente do primeiro número: ')

# print(f'O cálculo de {base} elevado ao {expoente} é igual a: {float(base)**float(expoente):.0f}')



# LAÇO FOR
# base = int(input('Digite a base: '))
# expoente = int(input('Digite o expoente: '))
# resultado = 1

# for i in range(expoente):
#     resultado = resultado * base
#     print(i, resultado)
    
# print(resultado)



# LAÇO WHILE
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
resultado = 1
count = 1

while count <= expoente:
    resultado = resultado * base
    count += 1
    
print(resultado)