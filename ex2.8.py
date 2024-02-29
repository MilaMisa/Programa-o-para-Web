
def verifica_numero_real(string):
    caracteres_validos = "0123456789.-"
    ponto_decimal = False
    tem_sinal = False

    for char in string:
        if char not in caracteres_validos:
            return False
        if char == '.':
            if ponto_decimal:
                return False
            ponto_decimal = True
        if char == '-':
            if tem_sinal:
                return False
            if string.index(char) != 0:
                return False
            tem_sinal = True

    if len(string) == 1 and string[0] == '-':
        return False

    return True

numero = input("Digite um número real: ")
if verifica_numero_real(numero):
    print("É um número real.")
else:
    print("Não é um número real.")