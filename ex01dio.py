segundos = int(input())

minutos = segundos // 60 #TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = segundos // 3600 ** 2 #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))