# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

genero = input("Digite M para masculino ou F para feminino: ")
if genero.upper() == "M":
    print("Masculino")
elif genero.upper() == "F":
    print("Feminino")
else:
    print("Sexo inválido")