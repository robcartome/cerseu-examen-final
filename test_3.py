"""
3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que medirá el tiempo de
ejecución. Apoyarse importando la librería time
- Crear una función, por ejemplo, división de dos números para decorarla con
la función anterior.
- Usar la propiedad de N parámetros para la función a decorar (*, **) y
visualizar los resultados con un mínimo tres ejemplos.
Sugerencia: Usar sleep para visualizar mejor el tiempo de ejecución

"""

import time

def mesureTime(func):

    def calculator(*args, **kwargs):
        inicio = time.time()
        result = func(*args, **kwargs)
        print("Tiempo de ejecución es: {}".format(time.time() - inicio))
        return result
    return calculator

@mesureTime
def division(a, b):
    time.sleep(1)
    return a / b


print(division(10, 2))
print(division(100, 20))
print(division(1000, 212))
