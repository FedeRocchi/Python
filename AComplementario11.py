print("----------------------------------------")
print("AComplementario 11")
print("----------------------------------------")



s=0

print("Ingrese un número de terminos")
n=int(input())

for x=1 in range (1,n):

    if x % 2 == 0 :
        s=s-(1/x)
    else :
        s=s+(1/x)


print("La suma será ", s)