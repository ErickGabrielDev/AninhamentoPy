# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior 
# o segundo valor é maior
# não existe valor maior. os dois são iguais.

def comparar_numeros():
    primeiro_numero = int(input("Digite o primeiro número inteiro: "))
    segundo_numero = int(input("Digite o segundo número inteiro: "))

    if primeiro_numero > segundo_numero:
        print("O primeiro valor é maior.")
    elif segundo_numero > primeiro_numero:
        print("O segundo valor é maior.")
    else:
        print("Não existe valor maior. Os dois são iguais.")

comparar_numeros()

