print("Dados:")
nome = "Nicholas Lage"
altura = 1.92
peso = 84
imc = peso / (altura)**2

linha_1 = f'{nome} tem {altura:.2f} de altura' #as variaveis quando se poem um f de frente a uma str tem que ter as chaves para serem lidas como variaveis e não str
# :.2f isso signfica que depois do ponto no numero terão duas casas deciamais, ou seja, :.nf são n casas decimais
#além disso se colocarmos :,.nf ele coloca a virgula de separação de milhar
#exemplo: 1,000.00

linha_2 = f'pesa {peso:.2f} Kg e seu IMC é:'

linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

# print(nome, "tem ", altura, " de altura,")
# print("pesa ", peso, "Kg e seu IMC é:")
# print(imc)

