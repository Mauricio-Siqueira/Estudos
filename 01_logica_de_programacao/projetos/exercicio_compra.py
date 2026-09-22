"""
Faça uma lista de compra com lista
O usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de indeces inexistente na lista 
"""
import os

compras = []


while True:
    entrada = input("[i]nserir, [a]pagar, [l]istar, [s]air: ")

    if entrada == 'i': 
        item = input('Valor: ')
        compras.append(item)
        os.system('cls')
    elif entrada == 's':
        print("Saindo da lista.")
        break
    elif entrada == 'a':
        if len(compras) == 0:
            print('Nada para apagar, a lista esta vazia.')
        else:
            print('Itens disponiveis: ')
            for indice, nome in enumerate(compras):
                print(indice, nome)

            indece_str = input('Informe o indice que deseja apagar: ')

            try:
                indice = int(indece_str)
                del compras[indice]
            except:
                print('Não foi possivel apagar o indice. ')

    elif entrada == 'l':
        os.system('cls')

        if len(compras) == 0:
            print('Nada na lista')

        for indice, nome in enumerate(compras):
            print(indice, nome)
    else:
        print('Opção invalida, digite a informação valida.')
        