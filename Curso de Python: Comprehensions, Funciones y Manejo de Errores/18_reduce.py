import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)

"""
Reduce(fun, seq) tiene dos parametros:

1. Una función particular a aplicar a todos los elementos de una secuencia
2. Una secuencia de elementos.

Como funciona:

- Primero toma los dos primeros elementos de la secuencia y aplica la función particular.
- Toma el resultado anterior y a este valor mas el siguiente elemento de la secuencia le aplica la función particular.
- El proceso continua hasta que no tiene mas elementos.
- Retorna el resultado.
"""