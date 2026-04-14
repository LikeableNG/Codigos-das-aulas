"""
Fatiamento de strings
Olá Mundo
0123456789
-987654321

Fatiamento [início:fim:passo]
Obs.: O valor do 'fim' não é incluído no fatiamento
Passo é opcional, e tem valor padrão 1, mas posso escolher outro valor

    
Função len() -> Retorna o tamanho da string,
 ou seja, o número de caracteres
"""
variavel = 'Olá Mundo'

print(variavel[0:9])      

print(variavel[0:9:2])
#pega letra sim, letra não, ou seja, pula de 2 em 2,
#começa no zero, deposi vai pro dois, depois pro quatro
#e assim por diante

print(variavel[8])

print(variavel[::-1])
#pega a string e inverte ela, ou seja, começa do final para o início.

print(10 * '-')

print(len(variavel))
#realiza a contagem de caracteres da string, ou seja, o tamanho da string

print(len(variavel[0:9:2]))

#Por exemplo, se eu quiser tirar o final do nome de um documento, 
# por exemplo substituir o .pdf por .txt, eu posso fazer isso 
# utilizando o fatiamento, pegando a string do nome do documento 
# e fatiando ela até o -4, ou seja, até o ponto, e depois concatenar
# com a extensão que eu quero.