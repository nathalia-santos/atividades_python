#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

v = int(input('Por favor, digite um valor: '))
if v < 0:
    print(f'O número digitado foi {v} e é NEGATIVO')
else:
    print(f'O número digitado foi {v} e é POSITIVO')
