# Lista de números para evaluar.
numeros = [10, 15, 22, 33, 40, 51]

# Iteramos sobre cada número en la lista.
for numero in numeros:
    # Usamos el operador módulo `%` para determinar si el número es par.
    # Un número es par si el resto de la división entre el número y 2 es 0.
    if numero % 2 == 0:
        # Si el número es par, imprimimos un mensaje indicando que es par.
        print(f"El número {numero} es par.")
    else:
        # Si el número no es par, entonces es impar.
        # Imprimimos un mensaje indicando que es impar.
        print(f"El número {numero} es impar.")
