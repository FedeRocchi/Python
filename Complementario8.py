print("----------------------------")
print("Complementario 8")
print("----------------------------")

pi = 3.14

print("Ingrese valores del menú ")
print("1: Área del triangulo: ")
print("2: Área del círculo: ")
Opc = float(input())

if Opc == 1 :
    print("Área del triangulo")
    print("Ingrese el lado del triangulo")
    L = float(input())
    A = ((3 **0.5 )/ 4)* L**2
    print("El área del triangulo es: ", A)


elif Opc==2 :
    print("Área del circulo")
    print("Ingrese el radio del circulo ")
    R = float(input())
    C = pi * r**2
    print("El área del circulo es: ", C)
else : 
    print("Error")

