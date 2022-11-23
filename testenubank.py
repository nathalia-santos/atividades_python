
duracoes = []
total_dias = 0
max_horas_por_dia = 3.00
total_horas = sum(duracoes)

total_filmes = int(input('Quantos filmes são? '))
while len(duracoes) < total_filmes:
    duracoes.append(float(input('Qual a duração do filme? ')))

print(duracoes)
