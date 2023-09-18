#aula 3
nome = input('qual seu nome ')
idade = input('qual sua idade ')
if nome and idade:
    print(f'seu nome eh {nome}')
    print(f'seu nome invertido eh {nome[::-1]}')
if ' ' in nome:
    print('seu nome possui espaco')
else:
    print('seu nome  nao possui espaco')
print(f'seu nome possui {len(nome)} letras')
print(f'a primeira letra do seu nome eh {nome[0]}')
print(f'a ultima letra do seu nome eh {nome[-1]}')
