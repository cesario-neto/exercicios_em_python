"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
lista_com_numeros = [n1, n2, n3]
lista_com_numeros.sort(reverse=True)
print(lista_com_numeros)

# OU 

# lista = []
# qnt = 3

# for i in range(qnt):
#     elemento = float(input('Digite um número: '))
#     lista.append(elemento)

# lista.sort(reverse=True)
# print(lista)