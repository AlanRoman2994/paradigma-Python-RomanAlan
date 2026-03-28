# Lista de numeros
numeros = [1, 2, 3, 4, 5]
print("lista original:", numeros)

# funcion para elevar al cuadrado
def cuadrado(X):
    return X * X

# Aplicar funcion con map
cuadrados = list(map(cuadrado, numeros))
print(f"Cuadrados:", cuadrados)

# filtro de numeros pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Numeros pares:", pares)

# suma de todos los elementos
from functools import reduce

suma = reduce(lambda a, b: a + b, numeros)
print("Suma total;", suma)