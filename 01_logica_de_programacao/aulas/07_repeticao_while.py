"""
Rpetição
while (enquanto)
executa uma ação enquanto for verdedeira
break (parar) 
Para de executar a repetição, procurando o laço mais proximo dela
Caso o break estiver dentro de while, o laço sera while.
Em casos que existem dois while (um laço dentro do outro), o primeiro break encerra no laço interno
retornando para o externo. O segundo while é executado e encerra no break externo
"""

# condicao = True

# while condicao:
#     nome = input("Digite um nome: ")
#     print(f"Seu nome é {nome}")

#     break

"""
Caso tenha um if em seu laço para encerrar, ficaria deste modo
Digirando sair o laço acaba, pois a condição e verdedadeira 
e retorna para 
"""


# teste = True

# while teste:
#     nome01 = input("Digite um nome: ").strip().capitalize()
#     print(f"Seu nome é {nome01}")

#     if nome01 == "Sair":
#         break

# print("Você digitou sair, assim, saindo do repetição")

# print(">>>>>>>>>>>")

# contador = 0

# while contador < 10:
#     contador = contador + 1
#     print(contador)

# print("acabou")

print(">>>>>>>>>>")

# Utilizando o continue

contador = 0

while contador <= 100:
    contador += 1

    if contador == 7:
        print("numero 7 não será mostrado")
        continue

    if contador >= 10 and contador <= 27:
        print("Não mostrar os números", contador)
        continue

    print(contador)
    
    if contador == 40:
        break

print("acabou")

print(">>>>>>>>")

# while dentro de While

qtd_linha = 5
qtd_coluna = 5

linha = 1
while linha <= 5:
    coluna = 1
    while coluna <= qtd_coluna:
        print(f"{linha=} {coluna=}")
        coluna += 1 

    linha += 1


print("acabou")


# exercicio

nome = "Mauricio"

indice = 0
novo_nome= ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1

print(novo_nome)