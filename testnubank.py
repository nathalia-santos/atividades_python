
#n = 5
#def acharMinimoDeDias(duracoes):

duracoes = []
total_dias = 0
max_horas_por_dia = 3.00
total_filmes = int(input('Quantos filmes são? '))
while len(duracoes) < total_filmes:
    duracoes.append(float(input('Qual a duração do filme? ')))
total_horas = sum(duracoes)
print(total_horas)
while True:
    if total_horas <= max_horas_por_dia:
        total_horas -= max_horas_por_dia
        total_dias += 1
    else:
        break
#while True:
    #if total_horas <= max_horas_por_dia:
        #total_horas -= max_horas_por_dia
        #total_dias += 1
print(total_dias)






