import random

def jogo():

    aventureiro_vida = 100
    aventureiro_ataque = random.randint(10,20)
    aventureiro_defesa = random.randint(1,5)

    monstro_vida = random.randint(60,80)
    monstro_ataque = random.randint(20,30)

    print(f"Aventureiro: vida - {aventureiro_vida} - att {aventureiro_ataque} - def {aventureiro_defesa}")
    print(f"Monstro: vida - {monstro_vida} - att {monstro_ataque}")

    rodada = 1
    while True:
        print(f"Rodada {rodada}")

        monstro_vida -= random.randint(1,aventureiro_ataque)
        if monstro_vida <= 0:
            print("O monstro morreu!")
            break
        print(f"Monstro: vida - {monstro_vida} - att {monstro_ataque}")

        if monstro_ataque > aventureiro_defesa:
            aventureiro_vida -= random.randint(1,monstro_ataque) - aventureiro_defesa
            if aventureiro_vida <= 0:
                print("O aventureiro morreu!")
                break
            print(f"Aventureiro: vida - {aventureiro_vida} - att {aventureiro_ataque} - def {aventureiro_defesa}")
        rodada += 1
jogo()