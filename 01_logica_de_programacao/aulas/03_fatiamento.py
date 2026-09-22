"""
Fatiamento de strings
012345678
Olá mundo!
-987654321
Fatiamento [i:f:p] [::]
Obs: A função len retonra a quantidade de caracteres da str
"""

variavel = "Ola mundo!"
print(variavel[0:10:])


"""
Exercicio
Peça para o usuário digitar o nome 
Peça para o usuário digitar a idade
Se nome e idade forem digitados
    exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaço
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nomé é {letra}
Se nada for digitado em nom ou idade:
    exiba "Desculpa, você deixou o campos vazios"
"""

nome = input("Digite deu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' and nome:
        print(f'Seu nome contem espaço.')
    else:
        print(f'Não contem espaço.')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primaira letra de seu nome é {nome[0]}')
    print(f'A ultima letra de seu nome é {nome[-1]}')

else:
    print(f'Desculpa, você deixou o campos vazios')