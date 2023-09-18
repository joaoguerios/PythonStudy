#
NOME = 'luiz otavio'
tamanho_nome = len(NOME)
nome_diferente = ''
a = 0
while a < tamanho_nome:
    nome_diferente += f'{NOME[a]}*'
    a = a + 1
print(nome_diferente)
print('fim')
