nota1 = float(input("digite sua nota de português:"))
nota2 = float(input("digite sua nota de matematica:"))
nota3 = float(input("digite sua nota de logistica:"))

média = (nota1 + nota2 + nota3) / 3

#verificar a média
if média >= 7:
    print("O aluno foi APROVADO!!!")
elif média <= 5:
    print("O aluno esta em RECUPERAÇÂO!!!")
else:
    print("O aluno foi REPROVADO!!!")
    