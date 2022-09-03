n1 = float(input('Digite a nota da sua primeira avaliação: '))
n2 = float(input('Digite a nota da sua segunda avaliação: '))

m = n1+n2/2

print(f'RESULTADO DA MÉDIA: {m}')

if m >= 6:
  print(f'APROVADO')

else:
  print(f'REPROVADO')

