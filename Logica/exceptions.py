"""
try/except
(Tentar) try -> tentar execultar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Digite um número para dobramos: ')

try:
    print('Str: ', numero_str)
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um número.')
    
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
# else:
#     print('isso não é um número.')
