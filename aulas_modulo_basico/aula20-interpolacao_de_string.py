"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
juros = 0.05
variavel = '%s, o preço é R$%.2f, com juros de %.2f' % (nome, preco, juros)
print(variavel)

print('O hexadecimal de %d é %04X' % (1500, 1500)) 
#mais comuns são %04X e %08X

#Uma opção de de formatação