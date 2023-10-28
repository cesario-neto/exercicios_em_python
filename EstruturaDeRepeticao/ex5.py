"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
a = int(input('Digite a população do país A: '))
b = int(input('Digite a população do país B: '))
tempo = 0
taxa_crescimento_a = float(input('Digite a taxa de crescimento da população em % do país A: '))
taxa_crescimento_b = float(input('Digite a taxa de crescimento da população em % do país B: '))

while taxa_crescimento_a < 1 or taxa_crescimento_a > 100:
    print('Digite a taxa de crescimento entre 1 e 100')
    taxa_crescimento_a = float(input('Digite a taxa de crescimento da população em % do país A: '))

while taxa_crescimento_b < 1 or taxa_crescimento_b > 100:
    print('Digite a taxa de crescimento entre 1 e 100')
    taxa_crescimento_b = float(input('Digite a taxa de crescimento da população em % do país B: '))
    
    
while a <= b:
    a =+ a + (a * (taxa_crescimento_a / 100))
    b =+ b + (b * (taxa_crescimento_b / 100))
    tempo += 1
    
print(f'Em {tempo} anos, o país A vai passa o B em população')
