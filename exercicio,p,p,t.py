class Jogo:
    def __init__(self):
        self.opcoes = ['pedra', 'papel', 'tesoura']

    def jogar(self, jogador1, jogador2):
        if jogador1 not in self.opcoes or jogador2 not in self.opcoes:
            return "Entrada inválida! Você deve escolher entre 'pedra', 'papel' ou 'tesoura'."
        
        if jogador1 == jogador2:
            return "Empate!"
        elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'tesoura' and jogador2 == 'papel') or (jogador1 == 'papel' and jogador2 == 'pedra'):
            return "Jogador 1 ganha!"
        else:
            return "Jogador 2 ganha!"

def main():
    jogo = Jogo()
    while True:
        print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
        jogador1 = input("Jogador 1, faça sua escolha (pedra, papel, tesoura): ")
        jogador2 = input("Jogador 2, faça sua escolha (pedra, papel, tesoura): ")
        resultado = jogo.jogar(jogador1.lower(), jogador2.lower())
        print(resultado)
        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            break

if __name__ == "__main__":
    main()
