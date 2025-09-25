# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
while True:
    print("Bem vindo a webStore! uma loja que sempre indica o produto mais barato! rsrs")
    boneco = float(input("Digite o preço do boneco: R$"))
    camiseta = float(input("Digite o preço da camiseta: R$"))
    caneca = float(input("Digite o preço da caneca: R$"))
    if boneco < camiseta and boneco < caneca:
        print("Você deve comprar o boneco!")
    elif camiseta < boneco and camiseta < caneca:
        print("Você deve comprar a camiseta!")
    else:
        print("Você deve comprar a caneca!")
    sair = input("Deseja comparar os preços de outros produtos? (s/n): ")
    if sair.lower() != 's':
        print("ok, voce agora esta devendo R$100 para a loja por utilizar nossos serviços!")
        break
