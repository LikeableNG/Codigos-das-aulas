"""
Variaveis escritas em letras maiusculas são termos que
nunca vão ser alterados no código

Manter a simplicidade de um codigo., minimiazadno o espaçamento

colocar um "\" quebra a linha durante o código

"""

velocidade = 61 #velocidade do carro
local_carro = 90 #posição em que o carro está

RADAR_1 = 60 #velocidade do radar 1
LOCAL_1 = 100 #posição do radar 1
RADAR_RANGE = 1 #a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carros passou radar 1')

if local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_1):
    print('Carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_1) and \
    velocidade > RADAR_1:
    print('Carro multado')
"""
O código acima é completamente funcional,
porém muita linha para as mesmas coisas, 
portanto para organizar melhor
    
"""
print(20*"-")
velocidade_acima = velocidade >RADAR_1

dentro_do_limite_do_radar = local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_1)

if velocidade_acima:
    print('Velocidade carros passou radar 1')

if dentro_do_limite_do_radar:
    print('Carro passou do radar 1')

if velocidade_acima and dentro_do_limite_do_radar:
    print('Carro multado')