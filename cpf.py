cpf_original= input("Digite seu cpf sem pontuação: ")
# Criar uma variavel para guardar os nove primeiros digitos
cpf9=""
esp=1
for i in cpf_original:
    if esp>9:
        break
    esp=esp+1
    cpf9=cpf9+i

print(cpf9)

# Variavel que  contém os pesos de 10 á 2
peso10=10
# Variavel que ira guardar os resultados da multiplicação
resultado=0

for x in cpf9:
    resultado=resultado+(int(x)*peso10)
    peso10=peso10-1

# Variavel para guardar o resto da divisão
resto=0
resto=resultado%11
cpf10=cpf9
if resto<2:
    cpf10=cpf10+"0"
else:
    cpf10+cpf10+str(11-resto)

# Variavel com peso 11,que irá até 2
peso11=11

# Zerar a variavel resultado para o novo calculo
resultado=0
for x in cpf10:
    resultado=resultado+(int(x)*peso11)
    peso11=peso11-1


resto=resultado%11
cpf_calculado=cpf10

if resto<2:
    cpf_calculado=cpf_calculado+"0"
else:
    cpf_calculado=cpf_calculado+str(11-resto)

if cpf_original==cpf_calculado:
    print("CPF CORRETO!")
else:
    print("CPF INVÀLIDO!")
