#Operador lógico "or"
#Podemos utilzar ele para caso ao menos ma das condições seja verdadeira.
#O or ele usa curto-circuito, ou seja, se a primeira condição for verdadeira, ele nem avalia a segunda.
#Exemplo:  
a = 5
b = 10
c = 15
print(a < b or b > c)  # True, pois a primeira condição é verdadeira
print(a > b or b > c)  # False, pois ambas as condições são falsas
print(a < b or 0)      # True, pois a primeira condição é verdadeira
print(a > b or 0)      # 0, pois ambas as condições são falsas e 0 é considerado falsy