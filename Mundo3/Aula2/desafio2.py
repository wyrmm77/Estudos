valores = []
while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor Duplicado!')
    
    continuar = input('Continuar? [S/N]: ').lower()
    if continuar == 'n':
        break
valores.sort()
print(valores)