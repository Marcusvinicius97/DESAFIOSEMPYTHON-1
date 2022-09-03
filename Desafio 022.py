nome = str(input('Digite seu nome completo: ')).strip()

print('\n...Carregando informações...\n')
print(f'Seu nome em maiúsculo é: {nome.upper()}')
print(f'Seu nome em maiúsculo é: {nome.lower()}')
print(f"Total de letras no nome: {len(nome) - nome.count(' ')}")
#print(f'Total de letras do seu primeiro nome: {nome.find(" ")}')
#ou
print(f'O seu primeiro nome tem um total de: {len(nome.split()[0])}')







