#Operador lógico "and"
#O operador "and" retorna True se ambas as condições forem verdadeiras.
#Exemplo:
a = 5
b = 10
c = 15
print(a < b and b < c)  # True, pois ambas as condições são verdadeiras.

#Se qualquer valor for considaro falsy (0, "", None, False), o "and" retornará esse valor.
print(a > b and b < c)  # False, pois a primeira condição é falsa
print(a < b and 0)      # 0, pois 0 é considerado falsy