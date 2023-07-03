#se ocupa a mesma região de memória:

saldo = 100
limite = saldo

print("'Saldo' esta na mesma região de memória que 'Limite'?:", saldo is limite)

saldo = 100
limite = 110

print("'Saldo' esta na mesma região de memória que 'Limite'?:", saldo is limite)