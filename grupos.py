from random import shuffle
import tabulate
from time import sleep

participantes = []
favor =[]
contra =[]
while True: 
    try:
        tema = str(input('Qual o tema de hoje: '))
        qtdd = int(input('Digite a quantidade de integrantes: '))
    except: 
        print('Tente novamente, variável com valor errado.')
    for i in range(1,(qtdd+1)):
        pessoa = str(input('Digite o nome {}: '.format(i)))
        participantes.append(pessoa)
    #print(participantes)
    shuffle(participantes)
    #print(participantes)
    for i in range(0,len(participantes)): 
        if i%2==0:
            favor.append(participantes[i])
        else:
            contra.append(participantes[i])
    #print(favor)
    #print(contra)
    print('+----------------------------------+')
    print('TEMA: {}'.format(tema.upper()))
    print('+----------------------------------+')
    print('Sequência: A FAVOR X CONTRA')
    for a in range(0,(len(favor))):
        print('--------------------------')
        print('| {} - {} X {} |'.format(a+1, favor[a], contra[a]))
    print('--------------------------')
    break
    

