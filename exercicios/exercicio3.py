primeiro_valor = input("Digite um valor: ")
segundo_valor = input("DIgite outro valor: ")

if primeiro_valor > segundo_valor:
	taltal = primeiro_valor
	nham = segundo_valor
	
	print(taltal, "é maior que", nham)
	
elif primeiro_valor < segundo_valor:
	taltal = segundo_valor
	nham = primeiro_valor
	
	print(taltal, "é maior que", nham)

else:
	print(primeiro_valor, "é igual a", segundo_valor)
    