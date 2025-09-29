""" 18.
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida """

while True:
    data = input("Digite uma data no formato dd/mm/aaaa (ou 'sair' para encerrar): ")
    if data.lower() == 'sair':
        print("Encerrando o programa.")
        break
    try:
        dia, mes, ano = map(int, data.split('/'))
        if ano < 1 or mes < 1 or mes > 12 or dia < 1:
            raise ValueError
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia > 31:
                raise ValueError
        elif mes in [4, 6, 9, 11]:
            if dia > 30:
                raise ValueError
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    raise ValueError
            else:
                if dia > 28:
                    raise ValueError
        print(f"A data {data} é válida.")
    except ValueError:
        print(f"A data {data} é inválida. Tente novamente.")