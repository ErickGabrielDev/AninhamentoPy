# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

def calcular_prestacao(valor_casa, anos, salario):
    total_prestacoes = anos * 12
    prestacao_mensal = valor_casa / total_prestacoes
    return prestacao_mensal

valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
anos = int(input("Digite em quantos anos você vai pagar: "))

prestacao = calcular_prestacao(valor_casa, anos, salario)

limite_prestacao = salario * 0.30

print(f"\nO valor da prestação mensal será: R$ {prestacao:.2f}")

if prestacao > limite_prestacao:
    print("Empréstimo negado! A prestação mensal excede 30% do seu salário.")
else:
    print("Empréstimo aprovado! A prestação mensal está dentro do limite.")
