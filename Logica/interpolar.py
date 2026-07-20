"""
Interpolação basica de Strings 
s - Strinegs 
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
"""
nome = "Mauricio"
preco = 1000.958943
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %08X" % (1500, 1500))
"""

"""
Formatação basica de Strings
s - strings
d - int
f - float
.<número de dígitos>f
(Caracteres)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex: 0>-100,1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadessimal de 1500 é {1500:08x}')