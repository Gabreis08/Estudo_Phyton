# obter os numeros pares da lista e soma-los
num=[34,6,9,16,3,78,46,50]
resultado=0

for x in num:
    if x%2==0:
        resultado=resultado+x
        print(x)


print("-------------------------------------")
print("O resultado da soma é " +str(resultado))
