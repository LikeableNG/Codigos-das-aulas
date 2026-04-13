#if / elif / else
#se/ se não, então se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
#para estar dentro do bloco da condição tem que dar um Tab para que 
# o if saiba que aquilo é o que te que ser executado.

elif entrada == 'sair': 
    print('Você saiu do sistema.')
#elif podem ser vários, podendo checar várias condições. 
# Além disso ele leva em conta a primeira verdadeira. 
# Se vc tiver 3 elif, ele checa até achar o primeiro verdadeiro.

else:
    print('Comando desconhecido. Escreva "entrar" ou "sair".')

print('Fim do programa.')
#caso as condições forem satisfeitas ou não, o que vier depois 
# se não estiver nas partes condicionais será executado obrigatoriamente.