class ex.p,p,t:
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

jogo = Jogo()
print(jogo.jogar('pedra', 'tesoura'))  # Jogador 1 ganha!
