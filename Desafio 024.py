cid = str(input('Digite um nome de uma cidade: ')).strip()

print(f'A cidade possui o nome santos no inicio: {(cid[:6].upper()  == "SANTOS")or(cid[:6].lower()  == "santos")} ')

