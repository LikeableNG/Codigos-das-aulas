# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ') #input é para receber dados do usuário
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) 
int_numero_2 = int(numero_2)
#não é recomendado fazer a conversão diratemnte no input, 
#pois pode gerar erros e fica impossível de realizar um check se o valor 
# colocado pelo usuário é um número, como é desejado nesse caso

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')