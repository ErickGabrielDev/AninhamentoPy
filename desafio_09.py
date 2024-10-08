# Crie um programa que faça o computador jogar jokenpô com você.

import random

def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    jogador = input("Escolha: pedra, papel ou tesoura: ").strip().lower()
    
    if jogador not in opcoes:
        print("Opção inválida! Por favor, escolha entre pedra, papel ou tesoura.")
        return
    
    computador = random.choice(opcoes)
    
    print(f"\nVocê escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")
    
    if jogador == computador:
        print("Empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

jogar_jokenpo()
