num_i=input("Digite um número inicial: ")
num_f=input("Digite um número final: ")
 
# mudança global de tipo string para int(assim sendo possivel realizar a conta aritimética)
num_i=int(num_i)
num_f=int(num_f)

# Variavel para contar os numeros pares
qtd=0
while(num_i<=num_f):
    if num_i%2==0:
        print(num_i)
        qtd=qtd+1
    num_i=num_i+1

print("--------------------------")
print("A quantidade de pares é"+str(qtd))