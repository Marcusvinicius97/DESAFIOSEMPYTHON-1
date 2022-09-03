#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Velocidade do carro? '))

m = v*7

if v <= 80:
   print('SEM MULTA')
else:
   print(f'Você foi multado no valor de: R${m:.2F}')

