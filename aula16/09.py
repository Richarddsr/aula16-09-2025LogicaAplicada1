# Aula de resolução da questão 3

# menu
def main():
   choice = input("Bem vindo ao sistema de calculo de tempo! digite S para continuar, ou outra tecla para encerrar o programa: ")
   if choice.lower() == "s":
      cod()
    
    

# Declarações
# S_O inicial
def cod():
    while True:
     S_0 = float(input("Digite o valor da posição inicial em metros: "))
     v = float(input("Digite o valor da velocidade em m/s: "))

# time
     t = float(input("Digite o valor do tempo gasto no movimento em m/s: "))

     print(S_0, v, t)
     print("\n")
     print("Distancia percorrida de: ")

#distancia percorrida

     s = S_0 + (v*t)

     print(f"A distancia percorrida no movimento é {s}m/s")
     print("\n")
     choice = input("Deseja fazer outro cálculo? Digite S para sim ou outra tecla para encerrar: ")
     if choice.lower() != "s":
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
   main()

