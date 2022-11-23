#Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Por favor, digite um número: '))
n2 = int(input('Por favor, digite outro número: '))

if n1 > n2:
    print(f'O maior número digitado foi {n1}')
else:
    print(f'O maior número digitado foi {n2}')