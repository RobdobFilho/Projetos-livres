total = 0
num_de_amigos = 4
entradas = 37.99
pratoprincipal = 50
sobremesa = 12.45
bebidas = 5.99
total += entradas + pratoprincipal + sobremesa + bebidas
print('Conta ate agora: ', total)
gorjeta = total * 0.25
print('Gorjeta: ', gorjeta)
total += gorjeta
print('Total com a gorjeta: ',total)
contafinal = total / num_de_amigos
print('Conta por pessoa: ', contafinal)
cada_um_paga = round(contafinal,2)
print('Cada um paga: ', cada_um_paga)