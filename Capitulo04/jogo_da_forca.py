# importando os módulos
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')
        
# Função do Jogo
def game():
    limpa_tela()
    
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhendo a palavra de forma aleatória
    palavra = random.choice(palavras)
    
    # Criando os traços pela quantidade de letras da palavra
    letras_descobertas = ['_' for letra in palavra]
    
    # Número de chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []
    
    # Loop das tentativas de acertos
    while chances > 0:  
        # Mostrando as informações para o usuário
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", letras_erradas)
        
        # Capturando o input do usuário e convertendo em minúsculo.
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Verificando se a letra está na palavra escolhida
        if tentativa in palavra:
            # Atualizando os traços com a letra acertada
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            # Adicionando na lista as letras erradas
            letras_erradas.append(tentativa)
    
        # Verificando se ainda tem traços na palavra escolhida        
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    
    # O usuário não descobriu todas as letras
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
    game()