# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
while True:
    um = float(input("Digite o primeiro valor: "))
    dois = float(input("Digite o segundo valor: "))
    tres = float(input("Digite o terceiro valor: "))
    if um > dois and um > tres:
        print(f"O maior valor é: {um}")
        if dois < tres:
            print(f"O menor valor é: {dois}")
        else:
            print(f"O menor valor é: {tres}")
    elif dois > um and dois > tres:
        print(f"O maior valor é: {dois}")
        if um < tres:
            print(f"O menor valor é: {um}")
        else:
            print(f"O menor valor é: {tres}")
    else:
        print(f"O maior valor é: {tres}")
        if um < dois:
            print(f"O menor valor é: {um}")
        else:
            print(f"O menor valor é: {dois}")
