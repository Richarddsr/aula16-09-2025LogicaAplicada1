""" 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. """


print("=== CALCULADORA DE FOLHA DE PAGAMENTO ===")
print()

valor_hora = float(input("Digite o valor da sua hora trabalhada: R$ "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir_percentual = 0
    desconto_ir = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir_percentual = 10
    desconto_ir = salario_bruto * 0.10
else:
    ir_percentual = 20
    desconto_ir = salario_bruto * 0.20


desconto_sindicato = salario_bruto * 0.03  
fgts = salario_bruto * 0.11  
total_descontos = desconto_ir + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print("\n" + "="*50)
print("FOLHA DE PAGAMENTO")
print("="*50)
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas})        : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}%)                     : R$ {desconto_ir:.2f}")
print(f"(-) Sindicato (3%)               : R$ {desconto_sindicato:.2f}")
print(f"FGTS (11%)                       : R$ {fgts:.2f}")
print(f"Total de descontos               : R$ {total_descontos:.2f}")
print(f"Salário Líquido                  : R$ {salario_liquido:.2f}")
print("="*50)