valores = []
contador = 0

while True:
    v = valores.append(int(input('Digite um valor: ')))
    contador += 1

    continuar = input('Continuar? [S/N]: ').lower()
    if continuar == 'n':
        break
valores.sort(reverse=True)
print(f'A Quantidade de numeros digitados foi: {contador}')
print(f'A ordem da lista de forma decrescente é {valores}')
if 5 not in valores:
    print('O valor 5 não está na lista!')
else:
    print('O valor 5 está na lista!')