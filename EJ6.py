import math 

print("-----------------------")
print("Ejercicio 6")
print("-----------------------")

print("Ingrese las cordenada del punto A:")
AX = float(input("Ax: "))
AY = float(input("Ay: "))

print("Ingrese coordenadas del punto B: ")
BX = float(input("Bx: "))
BY = float(input("By: "))

#proceso

D = ( (AX-BX)**2 + (AY-BY)**2)**0.5

print("RESULTADO", D)