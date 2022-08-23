print("-------------------------------------")
print("AComplementarios 19")
print("-------------------------------------")



print("Ingrese la cantidad de empleados")
ce = int(input())

i = 1
smayor = 0

print("Ingrese los sueldos")

while i<=ce :
    suel=float(input())
    if suel>smayor :
        c=i
    

    i=i+1

print("El empleado número ", c, "es tiene el mayor sueldo, que es ", smayor)