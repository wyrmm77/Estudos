valores = []
pares = []
impares = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    continuar = input('Continuar? [S/N]: ').lower()
    if continuar == 'n':
        break
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(valores)
print(pares)
print(impares)