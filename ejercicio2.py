# Crear una función que dado dos números "a" y "b" devolver la suma de ambos sin utilizar el operador "+"
import operator

number1 = 5
number2 = 5

def sumar(number1, number2):
    # suma = operator.add(number1, number2)
    suma = sum([number1, number2])
    return suma

# mensaje de la suma 
resultado = sumar(number1, number2)
print("La suma de", number1, "y", number2, "es igual a:", resultado)
