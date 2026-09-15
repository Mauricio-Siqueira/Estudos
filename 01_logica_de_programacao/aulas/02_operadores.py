# and (e) or (ou) not(não)
# or - qualquer condição verdadeira avalia toda a expressão como verdadeira
# Se qual quer valor for considerado verdadeiro, a expressão inteira será
# avaliada naquele valor.
# São considerados Falsy
# 0.0.0 '' false
# Também existe o tipo none que é usado para representar um não valor

entrada = input("[E]ntrada [S]ainda: ")
senha_entrada = input("Senha: ")

senha_permitida = "123456"

if (entrada == "E" or entrada == "e" )and senha_entrada == senha_permitida:
    print("Entrou")
else:
    print("Sair")

print(">>>>>>>>>")
# Avaliação de curto circuito
print(True and 0 and True)

print(0 or False or 0 or "abc")

senha = input("Senha: ") or "Sem Senha"
print(senha)

print(">>>>>>>>>")
# O not é utilizado para inverter expressões
# not True = falso
# not False = Verdadeiro
print(not True) # false
print(not False) # True

# Operadorede in (enta entre) e not in (Não esta entre)
# Strings são interaveis 
# 0 1 2 3 4 5
# O t á v i o 
# -6 -5 -4 -3 -2 -1