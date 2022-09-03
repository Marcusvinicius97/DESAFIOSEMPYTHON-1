from random import randint

d = int(input('Digite um número escolhido pelo computador: '))
n = randint(0,5)

if d == n:
    print(f'ACERTOU, {n}')
else:
    print(f'ERROU, NÚMERO CORRETO: {n}')




