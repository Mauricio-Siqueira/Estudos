"""
Escopo da função em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançado
O escolo local é o escolpo onde apenas nomes do mesmo local podem ser alcançados
Rua (Global) Tudo o que fica solto no código, fora de qualquer função
Casa (Local) É tudo que vocês cria dentro de uma função
"""

x = 10

def minha_funcao():
    y = 20
    print("Dentro da função.")
    print(x)
    print(y)

minha_funcao()

print('Fora da função.')
print(x)
print(y) #Erro (NomeErro: name 'y' is not defined)

#Assim que a função termina de rodar, tudo o que foi criado dentro dela deixa de existir na memória