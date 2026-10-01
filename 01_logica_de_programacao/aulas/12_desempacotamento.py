'''
introdução ao desempacotamento + tuple (tupla)

_, _, lista2, *resto = ['Mauricio', 'Julio', 'Carlos']
# lista1, lista2, lista3 = lista
print(lista2, resto)

# tupla - lista mutavel 
# Um pouco mais eficiente que a lista. Quando criar uma lista e não precisar alterar, o melhor seria utilizar uma tupla.

nova_lista = ['Lucas', 'Marcella', 'João']
# nova_lista = list(nova_lista) # Convertendo tupla para lista
nova_lista = tuple(nova_lista) # Convertendo lista para tupla / Não faz sentido converter desta foram, pois seria somente criar uma lista um tupla
print(nova_lista[-1]) # Selecionando o ultimo nome da lista
print(nova_lista)
'''

# Desempacotamento em chamada de função

string = 'ABCD'
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = 'Python', 'e', 'legal'
listas = [

    #0          1
    ["Helena", "Nathalia"],#0
    #0
    ["Julia", ],#1
    #0          1
    ["Nicole", "Giovana", (0, 10, 20, 30, 40)],#2
]


#p, b, c, *_, ap, u = lista
#rint(p, u, ap)

print(*string)
print(*lista)
print(*tupla)
print(*listas, sep='\n')