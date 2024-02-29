nota1 = float(input("Digite a 1° nota do aluno:"))
nota2 = float(input("Digite a 2° nota do aluno:"))
nota3 = float(input("Digite a 3° nota do aluno:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
if nota1 == 10 or nota2 == 10 or nota3 == 10:
    print("Parabéns!")
