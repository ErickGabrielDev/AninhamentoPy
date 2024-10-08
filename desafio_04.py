# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

def verificar_alistamento(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    
    if idade < 18:
        anos_faltando = 18 - idade
        return f"Você ainda vai se alistar. Faltam {anos_faltando} anos para o alistamento."
    elif idade == 18:
        return "É a hora de se alistar!"
    else:
        anos_passados = idade - 18
        return f"Já passou do tempo do alistamento. Você está {anos_passados} anos atrasado."

ano_nascimento = int(input("Digite o ano de nascimento: "))

resultado = verificar_alistamento(ano_nascimento)

print(resultado)
