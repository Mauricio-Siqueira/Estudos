'''
Operação ternaria (Condicional de uma linha)
<valor> if <condição> else <Outro valor>
'''

#condicao = 10 == 11
#variavel = 'Valor' if condicao else 'Outro valor'
#print(variavel)
digito = 10 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)


print('Valor' if False else 'Outro valor' if True else 'Fim...')