nota= input("Digite a primeira nota: ")
nota2= input("Digite a segunda nota: ")
nota3= input("Digite a terceira nota: ")
nota4= input("Digite a quarta nota: ")
# Vamos converter as variaveis de notas para float
nota=float(nota)
nota2=float(nota2)
nota3=float(nota3)
nota4=float(nota4)

media=(nota+nota2+nota3+nota4)/4
# Se a nota media do aluno for igual o maior que 7, ele é aprovado 
# se a nota media for igual ou menor a 4, ele será reprovado
# senão, recuperação
if media>=7:
   print("Aprovado")
elif media<=4:
   print("Reprovado")
else:
   print("Recuperação")