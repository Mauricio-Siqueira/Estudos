'''
Dados mutáveis
= - copiado o valor (Imutáveis) 
= - aponta para o mesmo valro na memória (Mutável)
'''

lista_a = ['Mauricio', 'Luiza', 1, True, 1.2]
lista_b = lista_a.copy()

# outra lista armazenada em memória

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)