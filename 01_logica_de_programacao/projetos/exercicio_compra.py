"""
Faça uma lista de compra com lista
O usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de indeces inexistente na lista 
"""

compras = []


while True:
    entrada = input("[i]nserir, [a]pagar, [l]istar:")

    if entrada == 'i':
        item = input('Valor: ')
        compras.append(item)
        print('Você encolheu inserir')
    elif entrada == 'a':
        print('Você escolheu apagar')
    elif entrada == 'l':
        if len(compras) == 0:
            print('Você escolheu listar')
    else:
        print('Opção invalida, digite a informação valida.')