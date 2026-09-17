'''
introdução ao desempacotamento + tuple (tupla)
'''

_, _, lista2, *resto = ['Mauricio', 'Julio', 'Carlos']
# lista1, lista2, lista3 = lista
print(lista2, resto)

# tupla - lista mutavel 
# Um pouco mais eficiente que a lista. Quando criar uma lista e não precisar alterar, o melhor seria utilizar uma tupla.

nova_lista = ['Lucas', 'Marcella', 'João']
# nova_lista = list(nova_lista) # Convertendo tupla para lista
nova_lista = tuple(nova_lista) # Convertendo lista para tupla
print(nova_lista[-1]) # Selecionando o ultimo nome da lista
print(nova_lista)

