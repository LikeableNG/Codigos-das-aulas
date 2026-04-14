"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

#EXPLICAÇÂO EXCEPT:

#O except é usado para casos, onde o erro pode ocorrer, 
# e ao inves de so jogar o erro em vc, ele mostra a mensagem 
# que vc, coloca para ele mostra, ou seja na hora de deixar 
# um try e um except, no except, seria bom ter uma descrição 
# do que aconteceu, para o usuário entender o que aconteceu, 
# e não ficar só com a mensagem de erro, que as vezes pode 
# ser confusa para quem não tem conhecimento em programação.