"""
Fatiamento de strings
Olá Mundo
0123456789
-987654321

Fatiamento [início:fim:passo]
Obs.: O valor do 'fim' não é incluído no fatiamento
    
Função len() -> Retorna o tamanho da string, ou seja, o número de caracteres
"""
variavel = 'Olá Mundo'
print(variavel[0:9])      

print(variavel[0:9:2])    
print(variavel[8])
print(variavel[::-1])
print(10 * '-')
print(len(variavel))
print(len(variavel[0:9:2]))