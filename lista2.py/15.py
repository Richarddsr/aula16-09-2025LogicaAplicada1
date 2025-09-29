""" 15.
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser umtriângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes; """

while True:
    lado1 = float(input("Digite o valor do primeiro lado: "))
    lado2 = float(input("Digite o valor do segundo lado: "))
    lado3 = float(input("Digite o valor do terceiro lado: "))
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
        if lado1 == lado2 == lado3:
            print("Os lados formam um triângulo equilátero.")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Os lados formam um triângulo isósceles.")
        else:
            print("Os lados formam um triângulo escaleno.")
    else:
        print("Os valores não podem formar um triângulo.")
    sair = input("Deseja verificar outros lados? (s/n): ")
    if sair.lower() != 's':
        print("ok..")
        break