""" 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo: """

while True:
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segnda nota: "))
    media = nota1 + nota2 / 2
    if media >= 9.0:
        print(f"Sua média é {media} e seu conceito é A")
    elif 7.5 <= media < 9.0:
        print(f"Sua média é {media} e seu conceito é B")
    elif 6.0 <= media < 7.5:
        print(f"Sua média é {media} e seu conceito é C")
    elif 4.0 <= media < 6.0:
        print(f"Sua média é {media} e seu conceito é D")
    else:
        print(f"Sua média é {media} e seu conceito é E")
    sair = input("Deseja calcular a média de outro aluno? (s/n): ")
    if sair.lower() != 's':
        print("ok..")
        break