
ano = ' '
while ano != 'a':
    ano = str(input('Digite um ano para ver o século correspondente[digite A para interromper o programa]: ' ))
    if ano == 'a':
        print('Até a próxima!')
        break
    elif len(ano) == 4 and ano[2] == '0' and ano[3] == '0':
        print(f'O ano {ano} corresponde ao século {ano[0]}{ano[1]}')
    elif len(ano) == 3:
        print(f'O  ano {ano} corresponde ao século {ano[0]}')
    else:
        niniciais = ano[0] + ano[1]
        n1 = int(niniciais)
        soma = n1 + 1
        print(f'O ano {ano} corresponde ao século {soma}')