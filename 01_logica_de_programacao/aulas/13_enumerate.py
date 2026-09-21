
"""
enumerate = enumera iteráveis (indices)
"""
# [(0, 'Lucas'), (1, 'Marcella'), (2, 'João'), (3, 'Mauricio')]
lista = ['Lucas', 'Marcella', 'João']
lista.append("Mauricio")

# Podemos deixar esta declaração de fora, pois podemos jogar ele direto em for para criar varias enumerate
# lista_enumerada = enumerate(lista)
# Ex:
# for item in enumerate(lista):
#    print(item)

# Convertendo em lista
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

lista_enumerada = enumerate(lista)

# for item in lista_enumerada:
#    indice, nome = item
#    print(indice, nome)

# Podendo ser feito 

for indice, nome in enumerate(lista):
    print(indice, nome)

