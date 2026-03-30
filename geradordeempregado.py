primeironome = 'Roberto'
ultimonome = 'Filho'
nomecompleto = primeironome +' ' + ultimonome
endereco = 'Brasilia'
endereco += '- Distrito Federal '
idade = 20
infoempregado = nomecompleto + ' tem ' + str(idade) + ' anos de idade'
print(infoempregado)
anosexperiencia = 2
infoexperiencia = 'Experiencia: ' + str(anosexperiencia) + ' anos'
print(infoexperiencia)
posicao = 'Estudante de engenharia'
salario = 7500
cartoaoempregado = f'Empregado: {nomecompleto} | idade: {idade} | posição: {posicao} | salario: R${float(salario)}'
print(cartoaoempregado)
codigoempregado = 'DEV-2026-RF-001'
departamento = codigoempregado[0:3]
print(departamento)
codigoano = codigoempregado[4:8]
print(codigoano)
iniciais = codigoempregado[9:11]
print(iniciais)
