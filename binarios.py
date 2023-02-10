def decimal_para_binario(decimal):
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return print(binario)

entrada = int(input("Digite um número decimal inteiro para ser convertido para binário: "))
decimal_para_binario(entrada)
