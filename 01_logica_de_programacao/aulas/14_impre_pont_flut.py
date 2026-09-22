'''
imprecisão de ponto flutuante
Double-precision floating-point format 754
'''
import decimal

numero_01 = decimal.Decimal(0.1)
# numero_01 = 0.1
numero_02 = decimal.Decimal(0.7)
# numero_02 = 0.7
numero_03 = numero_01 + numero_02
print(numero_03)
print(f'{numero_03:.2f}')
print(round(numero_03, 2))
