#horario 
horario = input('que horas sao ')
horario = int(horario)
if horario >= 0 and horario <= 11 :
    print('bom dia')
elif horario >= 12 and horario <= 17:
    print('boa tarde')
elif horario >= 18:
    print('boa noite')
