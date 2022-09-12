

"""
Busca el último índice del elemento dado
  x: arreglo en el que se busca
  y: valor a buscar
  Resultado: último índice de y en x; -1 si no está
  Lanza ValueError si x es None
"""
def find_last(x, y):
    if x is None:
        raise ValueError
    i = len(x)-1
    while i >= 0:
        if x[i] == y:
            return i
        i = i - 1
    return -1


"""
Busca el último índice de cero
  x: arreglo en el que se busca
  Resultado: último índice de 0 en x; -1 si no está
  Lanza TypeError si x es None
"""
def last_zero(x):
    for i in range(0, len(x)):
        if x[i] == 0:
            return i
    return -1


"""
Cuenta la cantidad de ceros en el arreglo
  x: arreglo en el que se cuentan los ceros
  Resultado: número de ocurrencias de cero en x
  Lanza TypeError si x es None
"""
def count_zero(x):
    count = 0
    for i in range(1, len(x)):
        if x[i] == 0:
            count += 1
    return count


"""
Cuenta los elementos positivos en el arreglo
  x: arreglo en el que se cuentan los positivos
  Resultado: número de elementos positivos en x
  Lanza TypeError si x es None
"""
def count_positive(x):
    count = 0
    for i in range(0, len(x)):
        if x[i] >= 0:
            count += 1
    return count
