#Exercício Python 26: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez.

nome = str(input('Digite uma frase: ')).upper().strip()

print(f'A letra (a) aparece: {nome.count("A")}')
print(f'A primeira letra aparece na posição: {nome.find("A")+1}')
print(f'A última letra aparece na posição: {nome.rfind("A")+1}')
