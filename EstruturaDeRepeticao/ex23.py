"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

numero = int(input('Digite um número inteiro: '))
total_divisao = 0
primos = []
nao_primos = []


for x in range(1, (numero + 1)):
    count = 0
    for y in range(1, (numero + 1)):
        if x % y == 0:
            count += 1
        total_divisao += 1  
    
    if count > 2:
        nao_primos.append(x)
    else:
        primos.append(x)   
        
primos = str(primos)
primos = primos.replace('[', '')
primos = primos.replace(']', '')

nao_primos = str(nao_primos)
nao_primos = nao_primos.replace('[', '')
nao_primos = nao_primos.replace(']', '')
        
print(f'Os números primos são: {primos}')
print(f'Os números não primos são: {nao_primos}')
print(f'O total de divisões feitas foram: {total_divisao}')