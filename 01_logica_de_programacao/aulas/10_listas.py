'''
lista em Python

Tipode de lista -> Mutavel 
Suporta varios valores de qualquer tipo
Conhecimento reutilizaveis - indices e fatiamento 
Método úteis: 
....append - Adiciona um item ao final
....insert - Adiciona um item ao indice escolhido
....pop - Remove do final ou do indice escolhido
....dek - apaga um indice
....clear - limpa a lista
....extend - estende a lista
....+ - concatena lista

# Create, Read, Update, Delete
# Criar, Ler,  Alterar, Apagar = lista[i] (CRUD)
'''

#.........01234
#........-54321

# string = "ABCDE" # 5 Caracteres

# print (bool([])) falsy
# print (lista, type(lista))

#......... 0 .. 1.......2.................3....4
#.........-5...-4.......-3................-2...-1
# lista = ([123, True, "Mauricio Siqueira", 1.2, []])
# lista[-3] = "Maria" # daltera indice 2 para Maria
# print(lista)
# print(lista[2], type(lista[2]))

#

lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(2)
print(lista, "Removido,", ultimo_valor)

#

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)