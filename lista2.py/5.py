# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média do aluno é: {media}")
    if media >= 7.0:
        print("Aprovado")
    elif 5.0 <= media < 7.0:
        print("Recuperação")
    else:
        print("Reprovado")
    sair = input("Deseja calcular a média de outro aluno? (s/n): ")
    if sair.lower() != 's':
        print("ok")
        break
