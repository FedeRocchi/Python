print("------------------------------------------------------")
print("Complementario 7")
print("------------------------------------------------------")

print("Ingrese valores de la ecuacion cuadratica ")
num1 = float(input("Ingrese A: "))
num2 = float(input("Ingrese B: "))
num3 = float(input("Ingrese C: "))

d = num2**2 - 4*num1*num3


if d>0 :
    x1 = ((-b)+d**0.5)/2*num1
    x2 = ((-b)-d**0.5)/2*num1
    print("Raices reales", x1 , x2)
else :
    print("Raices irracionales")
