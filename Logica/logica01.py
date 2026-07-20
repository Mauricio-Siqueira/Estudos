# função print( "123" sep = " - ") Separador seria 0 "-"
# Usada para imprimir argumentos em codígo informato entre os parentêses
# Dentro dos parentêses, existe o sep, que seria o identificador de saparador 
# Ex: Se por lógica a separação é utilizado por "Virgula" mas o sep você escolhe o que seria o separador 
# Podemos adicionar o "end" em final do print, nele você informa se quiser colocar algum caracter no final ou não quebrar linha

print(123, 456, sep = " - ", end=" ## ")
print(10, 20, sep = " - ", end=" - ")
print(30 , 40, sep = " - ")
print(50, 60 , sep= " - ")
print("=========================================")

"""
DocString = ("""""")
Python = Linguagem de programação
Tipo de tipagem - Dinamica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas

"""
print(1234)

# Aspas simples
print('Mauricio')

# Aspas duplas
print("Mauricio")

# Escape
print('Mauricio "Siqueira"')

# r
print(r"Mauricio \"Siqueira\"")

print("=========================================")

# Tipo int e float
# int -> Número Inteiro
# O tipo int representa qualquer número, positivo ou negativo
# int sem sinal é considerado positivo.
print(11) # int
print(-11) # int
print(0)

# Float -> Número com ponto flutuante 
# O tipo float representa qualquer número, positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo
print(1.1) # Float
print(1.1, -2.2) # Float
print(0.0) # Float

# A função type mostra o tipo que o Python inferiu o valor
print(type("Mauricio"))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
print("=========================================")

# Tipo de dado bool (Boolean)
# Ao questinar algo em programação, só existe duas respostas possiveis: sim (True) ou Não (False).
# Existem Vários Operadores para "Questionar". Dentre eles o ==, que é um operador lógico
# que questiona se um valor é igual a outro. 
print(10 == 10) #Sim -> True (Verdedeiro)
print(10 == 11) # Não -> False (Falso)
print(type(10 == 10))
print("=========================================")

# Conversão de tipos, coerção, type conversion, typecasting, coercion. 
# Seria o ato de converter um tipo em outro.
# Tipos imutáveis e primitivos: 
# str, int, float, bool
print(int ("1"), type(int("1")))
print(type(float("1") + 1))
print(bool(''))
print(str(11) + 'b')

# Variaveis são usadas para salvar algo na memoria do coputador.
# PEPS: Inicie variáveis com letras minúsculas, pode usar números e underline _
# O sinal de  = seria o operador de atribuição. Ele é usado para atribuir um valor
# a um nome (cariável)
# Uso do nome_variável = expressão

"""nome = 'Mauricio'
idade = 25
idade_minima = idade >= 18
print("Nome: ", nome, "Idade: ", idade)
print("É maior?", idade_minima)
"""
print(">>>>>>>>>>>>>>>")

nome = "Mauricio"
sobrenome = "Siqueira"
idade = 22
ano_nascimento = 2026 - idade
maior_de_idade = idade >= 18
altura_em_metros = 1.70

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print('É maior de idade: ', maior_de_idade)
print(f'Altura em metros: {altura_em_metros:.2f}')


"""
Operadores Lógicos

> Maior 
>= Maior ou igual 
< Menor
<= Menor ou igul
== Igual
!= Diferente
"""
print(">>>>>>>>>>>>>>>")

maior = 2 > 1
maior_igual = 2 >= 2
menor = 1 < 2
menor_igual = 2 <= 2
igual = "a" == "a"
diferente = "a" != "b"
print(maior)
