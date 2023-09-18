#aula4

velocidade = int(input('qual a velocidade'))
local_carro = int(input('onde o carro esta'))

RADAR1 = 60
LOCAL1 = 100
RADAR_RANGE = 1


if local_carro > (LOCAL1-RADAR_RANGE) or local_carro < (LOCAL1-RADAR_RANGE):
    print('o carro esta fora do radar')
else:
    if velocidade > RADAR1:
        print('voce foi multado')
    else:
        print('a velocidade esta dentro do padrao')
