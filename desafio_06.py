# A confederação nacional de notação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil 
# Até 19anos: Junior 
# Até 20 anos: Sênior
# Acima: Master

from datetime import datetime

def determinar_categoria(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    
    if idade <= 9:
        return "Mirim"
    elif idade <= 14:
        return "Infantil"
    elif idade <= 19:
        return "Junior"
    elif idade == 20:
        return "Sênior"
    else:
        return "Master"

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

categoria = determinar_categoria(ano_nascimento)

print(f"O atleta tem {datetime.now().year - ano_nascimento} anos e está na categoria: {categoria}.")
