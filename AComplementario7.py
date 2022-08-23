print("----------------------------------")
print("AComplementario 7")
print("----------------------------------")

C = 0

print("Ingrese 10 números enteros")
for x=1 in range (1,10 + 1):

    num1=int(input())
    
    if ( num1 % 2 == 0 ) :
        c = c+1
    break

print("Hay ", c, "numeros pares")
