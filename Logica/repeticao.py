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


teste = True

while teste:
    nome01 = input("Digite um nome: ").strip().capitalize()
    print(f"Seu nome é {nome01}")

    if nome01 == "Sair":
        break

print("Você digitou sair, assim, saindo do repetição")
