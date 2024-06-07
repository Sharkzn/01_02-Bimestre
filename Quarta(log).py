# calculadora de média
nota1 = float(input("Digite a nota 1: "))

nota2 = float(input("Digite a nota 2: "))

resultado = (nota1 + nota2) / 2

print("a media foi: " + str(resultado))

# verificar se o aluno foi aprovado ou reprovado 
if(resultado >= 7):
    print("aluno aprovado ")
else:
    print("aluno reprovado ")
