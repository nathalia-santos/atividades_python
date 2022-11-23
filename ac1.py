valor_produto = float(input('Valor: '))
quantidade = int(input('Quantidade: '))

desconto_fixo = 0.11
total_sem_desconto = valor_produto * quantidade
total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto_fixo)

print('%.2f' % total_sem_desconto)
print('%.2f' % total_com_desconto)

