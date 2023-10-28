"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n~ésimo termo.
"""
anterior = 0
proximo = 1
count = 0

while count < 10:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    count += 1