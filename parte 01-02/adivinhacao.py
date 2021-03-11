from random import randrange

def jogar_adivinhacao():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print("""
    ## Nivel de dificuldade ## 
    [ 1 ] Facil
    [ 2 ] Medio 
    [ 3 ] Dificil
    """)
    numero_secreto = randrange(0, 100)
    pontos = 1000
    opc = int(input("Digite a opção desejada: "))
    if opc == 1:
        tentativas = 10
    elif opc == 2:
        tentativas = 7
    elif opc == 3:
        tentativas = 5
    else:
        print("opção invalida")
        

    for c in range(0, tentativas):
        print(f"Tentativa {c + 1} de {tentativas}")
        chute = int(input("Digite o seu número: "))
        print(f"Você digitou: {chute}")
        

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if 1 < chute > 100:
            print("Numero invalido")
            print("Digite somente numeros entre 1 e 10")
            continue

        elif acertou:
            print("Você acertou!")
            print(f'E fez {pontos} pontos')
            break
        else:
            print("Você errou!")
            if maior:
                print(f"O numero secreto e menor do que {chute}")
            elif menor:
                print(f"O numero secreto e maior do que o {chute}")
            pontosperdidos = abs(numero_secreto - chute)
            pontos = pontos - pontosperdidos
        
print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()