"""
Argumentos nomeeados e não nomeados em funcção Python
Argumentos nomeadados tem o nome com sinal de igual (=)
Argumento não nomeados recebem apenas o argumento (Valor)
"""

# def some(x, y, z):
#     print(f'{x=} {y=} {z=}','|','x + y + z =', x + y + z)

# some(1, 2, 3)
# some(1, y=2, z=3)

# print(1, 2, 3, sep='-')

"""
Valores padrão para parametros
Ao Definir uma função, os parametros podem ter valores padrão. Caso o valor não seja envaido para o parametro, o valor padrão sera usado.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + x)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 1)
soma(100, 200)
soma(1, 2, 3)
soma(x=4, y=3, z=8)

# def pedir_lanche(sanduiche, bebida):
#     print(f'Você pediu um {sanduiche} e uma {bebida}')

# pedir_lanche(bebida="Coca", sanduiche="Hambúrguer")