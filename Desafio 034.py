#Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.


s = float(input('Digite o valor do seu salário: '))

if s >= 1250:
  print(f'o Valor do salário com ajuste de 10%: R${(s*0.1)+s:.2f}')
else:
  print(f'o Valor do salário com ajuste de 15%: R${(s*0.15)+s:.2f}')

