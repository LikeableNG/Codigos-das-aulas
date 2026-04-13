#.format não entendi muito bem acho q vou ter q rever depois

a = "eu"
b = "tu"
c = "ele"

string = 'a = {} b = {} c = {}'
formato = string.format(a, b, c)
#Se não colocar valores dentro das chaves, ele vai seguir a sequência dos argumentos no format

print(formato)



d = "tchola"
e = "tigruinho"
f = "astorga"

string2 = 'd = {2} e = {0} f = {1}'
formato2 = string2.format(e, f, d)
#Colocando os números da sequência dos argumentos dentro das chaves, 
# ele pega o valor correspondente, 
# porém é sempre váido lembrar que a contagem começa no 0

print(formato2)




g = "alavanca"
h = "Kylo Ren"
i = "Kwid"

string3 = 'g = {nome1} h = {nome2} i = {nome3}'
formato3 = string3.format(nome1=g, nome2=h, nome3=i)
#Também é possível nomear os argumentos dentro do format
# e colocar esses nomes dentro das chaves

print(formato3)
