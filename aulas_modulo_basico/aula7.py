#aula sobre variaveis
# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) #converter str em int
print(type(float('1') + 1)) # tornar uma str em float
# se somarmos um float com um int, obteresmos um valor em float, pois o float é mais detalhado no quesito numerico.
print(bool(' '))# se colocarmos um espaço em branco, o valor sera True
print(bool('')) # string vazia é False
print(str(11.2) + 'b')#tranformar um int ou um float em str podemos concatenar ele com um str