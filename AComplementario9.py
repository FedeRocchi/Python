print("---------------------------------")
print("AComplementario 9")
print("---------------------------------")


b = 2

for i=2 in range (1,29):
    
    co = 0

    for a=2 in range (1,b/2):
        if (b % a == 0) :
            co=co+1
            a=b
        break

    if co==0 :
        print("El cubo de ", b " es: "b**3)
    
    b=b+1

