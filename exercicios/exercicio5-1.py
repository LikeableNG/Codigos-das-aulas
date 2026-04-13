numero = input("Digite um número inteiro: ")

try:
    numero_f = float(numero)

    numero_i  = int(numero_f)

    if numero_f != numero_i:
        print('O número que você digitou não é um inteiro')

    elif numero_i % 2 == 0:
        print('O número que você colocou é par')   
    
    elif numero_i % 2 != 0:
        print('O número que você colocou é ímpar')

except ValueError:
    print('O que você digitou não é um número inteiro')