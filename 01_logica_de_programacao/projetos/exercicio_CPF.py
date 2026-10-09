"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite o CPF: ').replace('.','').replace('-','')

if not cpf.isdigit():
    print('Não é possível consultar: o CPF deve conter apenas números!')
elif len(cpf) != 11:
    print('Não é possível consultar: o CPF deve conter exatamente 11 dígitos!')
else:
    nove_digitos = cpf[0:9]
    contador_regressivo = 10
    resultado_soma = 0

    for digito in nove_digitos:
        resultado_soma += int(digito) * contador_regressivo
        print('Digito:', digito, 'Contador:', contador_regressivo)
        contador_regressivo -= 1

    digito_1 = (resultado_soma * 10) % 11
    digito_1 = 0 if digito_1 > 9 else digito_1
    print(f'O Primeiro Dígito é: {digito_1}')

    # dez_digitos = cpf[0:10]
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_soma_2 = 0

    for digito in dez_digitos:
        resultado_soma_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_soma_2 * 10) % 11
    digito_2 = 0 if digito_2 > 9 else digito_2
    print(f'O Segundo dígito é: {digito_2}')

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf == cpf_gerado:
        print(f'CPF {cpf} é Válido!')
    else:
        print('CPF inválido')