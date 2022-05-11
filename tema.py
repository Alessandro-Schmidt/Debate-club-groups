import random
from time import sleep
pessoas = int(input('Digite a quantidade de participantes: '))
temas = []
for i in range(0, pessoas+1): 
    tema = str(input('Digite uma sugestão: '))
    temas.append(tema)
    
for a in range(0,5):
    print('.')
    sleep(1)
print('Tema: {}'.format(random.choice(temas)))