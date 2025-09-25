# 6. Faça um Programa que leia três números e mostre o maior deles.
while True:
    um = float(input("Digite o primeiro valor: "))
    dois = float(input("Digite o segundo valor: "))
    tres = float(input("Digite o terceiro valor: "))
    if um > dois and um > tres:
        print(f"O maior valor é: {um}")
    elif dois > um and dois > tres:
        print(f"O maior valor é: {dois}")
    else:
        print(f"O maior valor é: {tres}")
        
