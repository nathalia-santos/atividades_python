#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
soma = 0
for i in range(0, 4):
    n = int(input(f'Por favor, digite a nota do {i + 1}º bimestre aqui: '))
    notas.append(n)
for nota in notas:
    soma += nota
    media = soma / 4
print(f'A média das notas digitadas foi de {media}')