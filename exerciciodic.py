# Exercício - sistema de perguntas e respostas
contador = 0
erros = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print('pergunta:', pergunta['Pergunta'])
    print('-----------------------------------')
    contador = 1
    for opcoes in pergunta['Opções']:
        print(f'{contador}) {opcoes}')
        contador += 1
    resposta = input('qual a resposta?')
    if resposta == pergunta['Resposta']:
        print('parabens voce acertou')
    else:
        while resposta != pergunta['Resposta']:
            print('voce errou tente novamente')
            erros += 1
            resposta = input('qual a resposta?')
print()
print('parabens voce acabou o teste')
print(f'voce teve {erros} erros')          