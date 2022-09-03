x1 = float(input('Digite o valor da altura em metros: '))
y1 = float(input('Digite o valor da largura em metros: '))

print(f'\n-------------- DADOS OBTIDOS --------------')
print(f'\nAltura: {x1:.2f}m')
print(f'Largura: {y1:.2f}m')
print(f'O valor da área: {x1*y1:.2f}m²')
print(f'A quantidade de tinta que será necessária para pintá-la a área: {(x1*y1)*1/2:.2f} l')
