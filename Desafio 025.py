#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o nome completo: ')).strip()

print(f'Este nome possui o silva? {"SILVA" in nome.upper() or "silva" in nome.lower()} ')
