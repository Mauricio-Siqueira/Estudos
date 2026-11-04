def contagem_regressiva(numero):
    for i in range(numero, 0, -1):
        print(i)

contagem_regressiva(12)


print("_______________________________")

def contagem_regressiva_2(numeros):
    while True:
        print(numeros)
        numeros-=1
        if numeros < 1:
            break

contagem_regressiva_2(10)