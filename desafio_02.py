# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

def converter_numero(numero, base):
    if base == 1:  
        return bin(numero)[2:]  
    elif base == 2:  
        return oct(numero)[2:]  
    elif base == 3:  
        return hex(numero)[2:]  
    else:
        return None  

numero = int(input("Digite um número inteiro: "))

print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

base = int(input("Digite a opção desejada (1, 2 ou 3): "))

resultado = converter_numero(numero, base)

if resultado is not None:
    if base == 1:
        print(f"{numero} em binário é: {resultado}")
    elif base == 2:
        print(f"{numero} em octal é: {resultado}")
    elif base == 3:
        print(f"{numero} em hexadecimal é: {resultado}")
else:
    print("Opção de base inválida.")
