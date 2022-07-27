"""
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios e
imprimirlos por consola.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará lista para ordenar de mayor a menor la
lista que se creará en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlo por
consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola.
"""
import random


def generar_numeros_random():
    lista_random = []
    for i in range(10):
        num = random.randint(1, 100)
        lista_random.append(num)
    print(lista_random)
    return lista_random

def numeros_no_repetidos(lista):
    lista_no_repetidos = []
    for elem in lista:
        if not elem in lista_no_repetidos:
            lista_no_repetidos.append(elem)
    print(lista_no_repetidos)
    return lista_no_repetidos

def ordenar_lista(lista, order_por):
    if order_por == 'ASCENDENTE':
        return lista.sort()
    return lista.sort().reverse()

def mayor_numero(lista):
    lista.sort()
    return list[-1]

"""Lista numeros aleatorios"""
generar_numeros_random()

lista_numeros_random = generar_numeros_random()

"""Lista numeros no repetidos"""
lista_no_repetidos = numeros_no_repetidos(lista_numeros_random)

"""Lista Ordenada"""
ordenar_lista(lista_no_repetidos, 'ASCENDENTE')

"""Mayor numero"""
mayor_numero(lista_no_repetidos)
