"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
cont = 0
lista = []
while cont < 5:
    num = input('Digite um número: ')
    lista.append(num)
    cont += 1

soma = 0
for i in lista:
    soma = soma + int(i)
    
media = soma / len(lista)

print(f'A soma dos números digitados é {soma}\nA média dos números digitados é {media}')
