"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
lista = []

while True:
    num_digitado = input('Digite um número inteiro de 0 até 1000 ou (p) para parar: ')
    num_digitado = num_digitado.lower()
    if num_digitado == 'p':
        break
    try:
        num_digitado_temp = int(num_digitado)
        if num_digitado_temp < 0 or num_digitado_temp > 1000:
            print('Digite números inteiros de 0 até 1000.')
        else:
            lista.append(num_digitado)
    except:
        print('digite apenas números inteiros ou digite p para parar.')
    
nova_lista = [int(x) for x in lista]
nova_lista.sort()

print(f'\nO Menor número que você digitou é {nova_lista[0]:.0f}\nO maior número digitado é {nova_lista[-1]:.0f}\nA soma de todos os números digitados é {sum(nova_lista):.0f}')