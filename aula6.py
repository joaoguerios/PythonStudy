#nome
nome = input('digite seu nome')
TAMANHO = len(nome)
if TAMANHO <= 4:
    print('seu nome eh curto')
elif TAMANHO == 5 or TAMANHO == 6:
    print('seu nome eh normal')
elif TAMANHO >6:
    print('seu nome eh grande')
