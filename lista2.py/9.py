# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente
numeors = []
um = float(input("Digite o primeiro valor: "))
numeors.append(um)
dois = float(input("Digite o segundo valor: "))
numeors.append(dois)
tres = float(input("Digite o terceiro valor: "))
numeors.append(tres)
print(sorted(numeors, reverse=True))
