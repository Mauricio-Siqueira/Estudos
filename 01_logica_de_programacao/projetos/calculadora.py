while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador(+, -, *, /): ")

    numero_valido = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print("Um ou ambos números digitados são invalidos")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Digite apenas um operador")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    print("Realizado sua conta. Confira o resultado")

    if operador == "+":
        print(num_1_float + num_2_float)

    elif operador == "-":
        print(num_1_float - num_2_float)

    elif operador == "/":
        print(num_1_float / num_2_float)

    elif operador == "*":
       print(num_1_float * num_2_float)
    else:
        print("Não era ára ter chegado aqui")    
    

    sair = input("Quer sair? Digite [s]air: ").lower().startswith("s")

    if sair is True:
        print("Você saiu")
        break