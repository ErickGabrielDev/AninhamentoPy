# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 20 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def obter_status(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso ideal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 40:
        return "Obesidade"
    else:
        return "Obesidade mórbida"

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = calcular_imc(peso, altura)

status = obter_status(imc)

print(f"Seu IMC é: {imc:.2f}")
print(f"Status: {status}")
