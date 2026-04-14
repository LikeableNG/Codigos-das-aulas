
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') 
#preenche com espaços a esquerda, totalizando 10 caracteres

print(f'{variavel: <10}.')
#preenche com espaços a direita, totalizando 10 caracteres

print(f'{variavel: ^10}.')
#preenche com espaços a esquerda e direita, totalizando 10 caracteres

#Nesses casos, eu utilizei o espaço como o caractere a ser utilizado,
#  mas se eu colocasse um outro caractere, entre os : >,< ou ^, 
# ele utilizaria desse para completar

print(f'{1000.4873648123746:0=+10,.1f}')
#O zero é para completar com zeros, o sinal é para mostrar o sinal positivo ou negativo,
# o 10 é para totalizar 10 caracteres, a vírgula é para separar os milhares.

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')