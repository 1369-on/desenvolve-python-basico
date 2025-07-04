
import random

def escolher_palavra():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.read().split("====")
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_forca():
    palavra = escolher_palavra()
    estagios = carregar_enforcado()
    palavra_oculta = ["_" for _ in palavra]
    letras_erradas = []
    erros = 0
    
    while erros < 6 and "_" in palavra_oculta:
        print(" ".join(palavra_oculta))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        chute = input("Digite uma letra: ").lower()
        
        if chute in palavra:
            for i, letra in enumerate(palavra):
                if letra == chute:
                    palavra_oculta[i] = letra
        else:
            erros += 1
            letras_erradas.append(chute)
            imprime_enforcado(erros, estagios)
    
    if "_" not in palavra_oculta:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

jogo_forca()
