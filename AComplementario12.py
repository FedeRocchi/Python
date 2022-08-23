print("-------------------------------------")
print("AComplementario 12")
print("-------------------------------------")



aux = 0
aux2 = 0
i = n

print("Ingrese un número")
n = int(input())

for i=10 in range (1,n):

    aux = i%10
    i = i//10
    aux2 = aux*10+aux

aux2 = aux2*10+i

print("El número invertido será: ", aux2)