# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

def calcular_preco(preco, forma_pagamento, parcelas=1):
    if forma_pagamento == 1: 
        desconto = 0.10
        preco_final = preco * (1 - desconto)
    elif forma_pagamento == 2:  
        desconto = 0.05
        preco_final = preco * (1 - desconto)
    elif forma_pagamento == 3:  
        preco_final = preco  
    elif forma_pagamento == 4:  
        juros = 0.20
        preco_final = preco * (1 + juros)
    else:
        return None  

    return preco_final

preco = float(input("Digite o preço do produto: R$ "))

print("Escolha a forma de pagamento:")
print("1 - À vista dinheiro/cheque")
print("2 - À vista no cartão")
print("3 - Em até 2x no cartão")
print("4 - 3x ou mais no cartão")

forma_pagamento = int(input("Digite a opção desejada (1, 2, 3 ou 4): "))

parcelas = 1  

if forma_pagamento in [3, 4]:
    parcelas = int(input("Digite o número de parcelas: "))

    if forma_pagamento == 3 and parcelas > 2:
        print("Para essa opção, você só pode parcelar em até 2x.")
        parcelas = 2 
    elif forma_pagamento == 4 and parcelas < 3:
        print("Para essa opção, você deve parcelar em 3x ou mais.")
        parcelas = 3  

preco_final = calcular_preco(preco, forma_pagamento, parcelas)

if preco_final is not None:
    print(f"O valor a ser pago é: R$ {preco_final:.2f}")
else:
    print("Opção de pagamento inválida.")
