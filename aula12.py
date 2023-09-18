#lista de compras
lista =[]
while True:
    escolha = input(print('[1] adicionar  [2] excluir  [3] ver a lista  para encerrar digite fim=>'))
    if escolha == '1':
        adicionar = input('digite oque deseja adicionar na lista =>')
        lista.append(adicionar)
    elif escolha == '2':
        indice = input('qual o indice do produto que deseja retirar da lista =>')
        try:
            indice = int(indice)
            lista.pop(indice)
        except Exception:
            print('digite um indice que esta dentro da lista')
    elif escolha == '3':
        for i, valor in enumerate(lista):
            print(i, valor)
    elif escolha =='fim':
        break
    else:
        print('escolha uma opcao valida')
