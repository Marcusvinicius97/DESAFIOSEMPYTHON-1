import random
n = []
while True:
  n.append(str(input('Digite o nome do aluno: ')))
  x = input('Deseja acrescentar mais alunos sim ou não? ').upper()[0]
  if x == 'N':
   break
random.shuffle(n)
print(f'O aluno sorteado é: {n[0]}')
