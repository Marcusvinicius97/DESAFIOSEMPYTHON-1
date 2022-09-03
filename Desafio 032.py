#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

a = int(input('Digite o ano: '))

if a % 4 == 0:
   print(f'Ano bisssexto')
else:
    print(f'Não é um ano Bissexto')


