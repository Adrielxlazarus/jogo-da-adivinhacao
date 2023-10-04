from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "Pensar"
print('-=-' *20)
print("Vou pensar em um numero entre 0 e 10. Tente adivinhar ele...")
print('-=-' *20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('Processando...')
sleep(5)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print("GANHEI! Eu pensei no número {} e não no {}! kkkk".format(computador, jogador))