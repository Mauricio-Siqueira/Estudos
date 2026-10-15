"""
Introdução em funções (def) em python
Funções são trechos de códigos usadas para replicar determinadas ações ao longo do código.
Elas pode receber valores para parâmetros (argumentos)
e retornar um valro especifico
Por padrão, funções retornam None em Python (nada).
"""

def saudacao(nome="Sem nome"):
    print(f'Ola {nome}!')

saudacao("Mauricio")
saudacao ("João")
saudacao("Marcos")
saudacao()

# def numero():
#     print("Variavel1")
#     print("Variavel2")
#     print("Variavel3")
#     print("Variavel4")

# numero()

# def imprimir(a, b, c):
#     print(a, b, c)
    
# imprimir(1, 2, 3)