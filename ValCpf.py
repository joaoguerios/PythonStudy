# algoritimo de criacao e validacao de cpf
# 0  1  2  3  4  5  6  7  8   9  10
# 0  7  0  0  8  1  3  5  9  -4  7
# 10 9  8  7  6  5  4  3  2  -v  v
escolha = input('Você deseja conferir um CPF (A) ou criar um CPF (B)? => ')
escolha = escolha.upper()

while escolha != 'B' and escolha != 'A':
    print('Opção não encontrada.')
    escolha = input('Você deseja conferir um CPF (A) ou criar um CPF (B)? => ')
    escolha = escolha.upper()

# Aqui, a escolha válida foi feita (B ou A)
if escolha == 'B':
    # Código para criar um CPF
    print('Opção B selecionada. Criar CPF...')
elif escolha == 'A':
    # Código para conferir um CPF
    print('Opção A selecionada. Conferir CPF...')


if escolha == 'A':

    multiplicador1 = 10  # define o multiplicador para verificar o primeiro digito verificador
    soma = 0
    cpf = input('digite o cpf que voce deseja validar(apenas os numeros)=>')

    # enquanto o tam do cpf for direfrente de 11 repete
    while len(cpf) != 11 or cpf.isdigit() is False:
        print('por favor confiro o numero de numeros do cpf digitado')
        cpf = input(
            'digite o cpf que voce deseja validar(apenas os numeros) =>')
    print(cpf[:9])
    digitos = cpf[:9]

    for numero in digitos:
        numero = int(numero)  # transforma para int para poder multiplicar
        soma = soma + (numero * multiplicador1)
        multiplicador1 -= 1

    val1 = (soma) % 11
    if val1 > 9:
        Verificador1 = 0
    else:
        verificador1 = 11 - val1

    print(f'primeiro verificador = {verificador1}')
    # ----------------- fim do verificador 1 ----------------------

    soma = 0
    multiplicador2 = 11
    digitos = cpf[:10]

    for numero in digitos:
        numero = int(numero)  # transforma para int para poder multiplicar
        soma = soma + (numero * multiplicador2)
        multiplicador2 -= 1

    val2 = (soma) % 11
    if val2 > 9:
        verificador2 = 0
    else:
        verificador2 = 11 - val2

    print(f'segundo verificador = {verificador2}')
    # ----------------- fim do verificador 2 ----------------------

    # transforma em string para poder comparar
    verificador1 = str(verificador1)
    verificador2 = str(verificador2)  # transforma em string para comparar

    if verificador2 == cpf[10] and verificador1 == cpf[9]:
        print(f'o cpf {cpf} e valido')
    elif verificador2 != cpf[11] and verificador1 == cpf[10]:
        print(f'o verificador2 seria {verificador2}')
    elif verificador2 == cpf[11] and verificador1 != cpf[10]:
        print(f'o verificador1 seria {verificador1}')
    else:
        print(f'o cpf {cpf} eh invalido')

else:  # ---------------- comeco da opcao (B) -------------------

    multiplicador1 = 10
    soma = 0

    cpf = input(
        'digite os primeiros 9 digitos do cpf que voce deseja criar(apenas os numeros) =>')
    # enquanto o tam do cpf for direfrente de 11 repete
    while len(cpf) != 9 or cpf.isdigit() is False:
        print('por favor confira o numero de numeros do cpf digitado')
        cpf = input(
            'digite o cpf que voce deseja validar(apenas os numeros) =>')
    print(cpf[:9])
    digitos = cpf[:9]

    for numero in digitos:
        numero = int(numero)  # transforma para int para poder multiplicar
        soma = soma + (numero * multiplicador1)
        multiplicador1 -= 1

    val1 = (soma) % 11

    if val1 > 9:
        Verificador1 = 0
    else:
        verificador1 = 11 - val1

    print(f'primeiro verificador = {verificador1}')
    # transforma em string para poder concatenar
    verificador1 = str(verificador1)
    cpf = cpf + verificador1
    # ----------------- fim do verificador 1 ----------------------
    soma = 0
    multiplicador2 = 11
    digitos = cpf[:10]
    for numero in digitos:
        numero = int(numero)  # transforma para int para poder multiplicar
        soma = soma + (numero * multiplicador2)
        multiplicador2 -= 1

    val2 = (soma) % 11
    if val2 > 9:
        verificador2 = 0
    else:
        verificador2 = 11 - val2

    print(f'segundo verificador = {verificador2}')
    verificador2 = str(verificador2)  # transforma em string para concatenar
    # ----------------- fim do verificador 2 ----------------------

    cpf = cpf + verificador2
    print(f'o cpf gerado foi {cpf}')
