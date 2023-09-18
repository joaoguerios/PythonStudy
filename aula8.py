#calc com while
while  True:
    nu1 = int(input('digite o primeiro numero '))
    nu2 = int(input('digite o segundo numero '))
    op = input('digite o operador que voce deseja +, -, *, / ')
    if len(op)>1:
        print('digite apenas 1 operador')
    if op == '+':
        resultado = nu1 + nu2
        print(resultado)
    elif op == '-':
        resultado = nu1 - nu2
        print(resultado)
    elif op == '*':
        resultado = nu1 * nu2
        print(resultado)
    elif op == '/':
        resultado = nu1 / nu2
        print(resultado)
    else:
        print('operacao invalida')
    sair = input('deseja sair: [s] [n]')
    sair = sair.lower
    if sair == 's':
        break
