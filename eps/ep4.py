# Ler data
d = int(input("dia: ")) 
mes = int(input("mes: "))
ano = int(input("ano: "))
#Ajuste para janiero e fevereiro serem respectivamente 13 e 14, pois mes<3 é um bool que quando int vira 1(True) e 0 (False)
ajuste = int(mes < 3)
#Corrijindo mes e ano
m = mes + (ajuste*12)
a = ano - ajuste

# Calcular dia da semana
s = (d + ((13 * (m + 1)) // 5) + a + (a // 4) - (a // 100) + (a // 400)) % 7
# Exibir resposta
print( s ) 