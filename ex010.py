#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
# fórmula: (72.7*altura) - 58

altura = float(input('Por favor, digite sua altura: '))
peso_ideal = (72.7 * altura) - 58
print(f'De acordo com a sua altura de {altura}, seu peso ideal é {peso_ideal:.2f}')