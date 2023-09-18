#
nome = 'joao'
sobrenome = 'guerios'
idade = 18
ano_nascimento = 2005
MaiorDeIdade = idade >= 18
altura = 1.8
peso = 95

f1 = f'seu nome: {nome} {sobrenome}'

print('seu nome: ', nome,sobrenome)
print('voce tem', idade, 'nasceu em', ano_nascimento)
print('voce mede', altura)
if MaiorDeIdade == True:
    print('voce eh maior de idade')
else:
    print('voce eh menor de idade')
imc = peso / (altura * altura)
print('seu imc: ',imc)
print(f1)
