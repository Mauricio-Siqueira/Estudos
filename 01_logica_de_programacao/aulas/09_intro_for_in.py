"""
senha_salve = "1234"
senha_digitada = " "
repeticoes = 0

while senha_salve != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}): ')

    repeticoes += 1

print(repeticoes)
"""

# For = Para, in = em
# Em codígo: Para cada (letra) em (texto)

'''
texto = "Python"

novo_texto = " "
for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)
print(novo_texto + "*" )
'''

# for + range
# range -> range (Start, stop, step)
# Iteraval -> str, range, etc
# Iterador => Quem sabe entregar um valor por vez. Next -> Me entrega o proximo valor
# inter -> me entrega seu iterador

"""
numeros = range(0, 10, 2)

for numero in numeros:
    print(numero)
"""

"""
for i in range(10):
    if i == 2: 
        print("i é 2, pulando...")
        continue

    if i == 8:
        print("i é igual a 8 seu else não executará")
        break

    for j in range(1, 3):
        print(i, j)

else:
    print("For completo com sucesso")

"""

# palavra_secreta = "cachorro"
# letras_acertadas = ""
# numero_de_tentativas = 0

# while True:
#     letra_digitada = input("Digite uma letra: ")
#     numero_de_tentativas += 1

#     if len(letra_digitada) > 1:
#         print("Digite apenas uma letra.")
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ""

#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += "*"

#     print("palavra_formada", palavra_formada)

#     if palavra_formada == palavra_secreta:
#         print("Você acertou! Parabens!")
#         print("A palavra era", palavra_secreta)
#         print("tentativas:", numero_de_tentativas)

"""
for in com lista
"""

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))