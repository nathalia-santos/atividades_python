#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
# seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = str(input('Por favor, informe seu sexo biológico[F/M]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Por favor, informe seu sexo biológico[F/M]: ')).upper().strip()[0]
altura = float(input('Por favor, agora digite sua altura: '))
if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'De acordo com a altura digitada de {altura}, seu peso ideal é de {peso_ideal:.2f}')
else:
    peso_ideal = (72.7 * altura) - 58
    print(f'De acordo com altura digitada de {altura}, seu peso ideal é de {peso_ideal:.2f}')