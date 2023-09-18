#jogo da palavra tipo
import random
import os

LISTASECRETA = ('mexer','senso','afeto','sutil','inato','cerne','caixa','pedro','patos')
print('bem vindo ao jogo de acertar a palavra secreta')
print('o jogo consiste em voce acertar uma palvra formada por 5 letras')
print('====================================')
print('tipo 1 = jogo com chances limitadas')
print('')
print('tipo 2 = jogo com chances ilimitadas')
print('====================================')

TipoDoJogo = input('qual tipo de jogo voce quer jogar? =>')
while TipoDoJogo != '1' and TipoDoJogo != '2':
    print(f'{TipoDoJogo} nao disponivel, os tipos disponiveis sao apenas 1 e 2 ')
    TipoDoJogo = input('qual tipo de jogo voce quer jogar? =>')
print(f'tipo {TipoDoJogo} escolhido')

x = random.randint(0,9)
PAlAVRASECRETA = LISTASECRETA[x]
print(PAlAVRASECRETA)
tentativas = 0
LetrasCertas = ''
PalavraFormada = ''
contador = 0
if TipoDoJogo == '1':
    while tentativas < 8 and LetrasCertas != PAlAVRASECRETA :
        tentativas = tentativas + 1
        print(f'tentativa numero {tentativas}')
        letra = input('digite uma letra')
        contador += 1
        if letra in PAlAVRASECRETA:
            LetrasCertas += letra
        for letra_secreta in PAlAVRASECRETA:
            if letra_secreta in LetrasCertas:
                print(letra_secreta)
            else:
                print('*')
else:
    while LetrasCertas != PAlAVRASECRETA :
        tentativas = tentativas + 1
        print(f'tentativa numero {tentativas}')
        letra = input('digite uma letra')
        contador += 1
        if letra in PAlAVRASECRETA:
            LetrasCertas += letra
        for letra_secreta in PAlAVRASECRETA:
            if letra_secreta in LetrasCertas:
                print(letra_secreta)
            else:
                print('*')
        print (LetrasCertas)
os.system('clear')
print('parabens voce ganhou')
