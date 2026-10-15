"""
Argumentos nomeeados e não nomeados em funcção Python
Argumentos nomeadados tem o nome com sinal de igual (=)
Argumento não nomeados recebem apenas o argumento (Valor)
"""

def some(x, y, z):
    print(f'{x=} {y=} {z=}','|','x + y + z =', x + y + z)

some(1, 2, 3)
some(1, y=2, z=3)

print(1, 2, 3, sep='-')