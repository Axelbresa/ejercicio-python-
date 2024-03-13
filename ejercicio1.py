# Crear una función que dado un número "n" calcular su factorial sin utilizar el operador "*"


def calcular_factorial(n):
    if n < 0:
        return None 
    elif n == 0:
        return 1  
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado = multiplicar(resultado, i)
        return resultado

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado = sumar(resultado, a)
    return resultado

resultado = calcular_factorial(4)
print("El factorial de 5 es:", resultado)
