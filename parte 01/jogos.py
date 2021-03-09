import forca
import adivinhacao

def escolher_jogos():
    print("ESCOLHA O SEU JOGO")
    print("""
    [ 1 ] Forca
    [ 2 ] Adivinhção
    """)
    jogo = int(input("Escolha o seu jogo: "))
    if jogo == 1:
        forca.jogar_forca()
    elif jogo == 2:
        adivinhacao.jogar_adivinhacao()
if(__name__ == "__main__"):
    escolher_jogos()