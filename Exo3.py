# Exo 3
# a = int(input('Nombre 1 : '))
# b = int(input('Nombre 2 : '))
# operation = input('Opération ? parmi + - * / ')

# if operation == '+' :
#    print(a+b) 
# elif operation == '-' :
#         print(a-b)
# elif operation == '*' :
#         print(a*b)
        
# elif operation == '/' :
#         print(a/b)

# else : print('Veuillez choisir un bon opérateur')

# 2eme solutions

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division par zéro impossible"

operations = {
    '+': addition,
    '-': soustraction,
    '*': multiplication,
    '/': division
}
def calculatrice():
    a = int(input('Nombre 1 : '))
    b = int(input('Nombre 2 : '))
    operation = input('Opération ? parmi + - * / ')
    operation_func = operations.get(operation)
    
    if operation_func:
        resultat = operation_func(a, b)
    else:
        resultat = 'Veuillez choisir un bon opérateur'

    print("Résultat : ", resultat)
calculatrice()
