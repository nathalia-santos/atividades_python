#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('Por favor, digite um número inteiro: '))
n2 = int(input('Por favor, digite mais um número inteiro: '))
n3 = float(input('Por favor, digite um número real: '))

r1 = (n1 * 2) + (n2 / 2)
print(f'O dobro do número {n1} com metade do número {n2} é {r1}')
r2 = (n1 * 3) + n3
print(f'A soma do triplo de {n1} e {n3} é {r2}')
r3 = n3 ** 3
print(f'O {n3} elevado ao cubo é {r3:.2f}')
