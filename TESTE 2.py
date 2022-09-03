d = int(input('Qual a distância da sua viagem em Km? '))
if d <= 200:
    print(f'Sua viagem custará R${d*0.50:.2f}')
else:
    print(f'Sua viagem custará R${d*0.45:.2f}')

