entrada= input("Digite um número da tabuada: ")
n=1

while(n<=10):
    print(entrada + "x" + str(n) + "=" + str(int(entrada) * n))
    n=n+1