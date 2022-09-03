# Exibe a tabuada de um número digitado
n = int(input('Digite um número: '))
i = 0
print('=' * 15)
while i < 10:
    i = i + 1
    print(f'{n} x {i:5} = { n * i}')
print('=' * 15)