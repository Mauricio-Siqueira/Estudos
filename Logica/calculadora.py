while True:
    numero_01 = input("Digite um número: ")
    numero_02 = input("Digite outro número: ")
    operador = input("Digite um operador(+, -, *, /): ")

    numero_valido = None

    try:
        nun_1_ = float(numero_01)
        nun_2_ = float(numero_02)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print("Um ou ambos números digitados são invalidos")
        continue

    operadores_permitidos = "+-/*"
    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    sair = input("Quer sair? Digite [s]air: ").lower().startswith("s")

    if sair is True:
        print("Você saiu")
        break