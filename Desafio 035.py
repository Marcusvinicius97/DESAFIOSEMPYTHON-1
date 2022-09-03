n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

if (n2-n3) < n1 < n2+n3 and (n1 - n3) < n2 < n1+n3 and (n1-n2) < n3 < n1+n2:

    print('Os segmentos digitados podem formar um triângulo: ')

else:
    print(f'\33[0:33:40mOs valores digitados não podem formar um triângulo')

