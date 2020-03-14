#mim max algorithm to solve tictactoe
#Author Vinicius Franca

#https://www.geeksforgeeks.org/python-gui-tkinter/
#http://www.codekraft.co/freecodecamp/jogo-da-velha-entendendo-o-algoritimo-minimax/

class Game:
    def __init__(self, mode):
        self.state = [[]]
        self.mode = mode #true
        self.player = False #true for p1 and false for p3

    def start(self):
        self.state = [[0 for i in range(0, 3)] for c in range(0, 3)]
        self.show()
        self.pass_turn()

    def show(self):
        if self.player: print('\nPlayer 1')
        else: print('\nPlayer 2')

        for l in self.state:
            print(l)
        
        print('')

    def pass_turn(self):
        result = self.winner()
        if result[0]:
            print('*************************')
            print('The Game is over')
            print('The Winner is Player '+ result[1])
            self.show()
            print('*************************')
            return 

        if mode == 1 & self.player:
            l = input('\n*Insira a linha: ')
            c = input('\n*Insira a coluna: ')
            self.state[l][c] = 1
        
        self.generate_states(self.state, not self.player)

    def winner(self):
        # result linha
        for l in self.state:
            found = (l[0] == l[1] == l[2]) & (l[0] != -1)
            if found: 
                return found, l[0]

        # result column
        for l in range(len(self.state)):
            found = (self.state[l][0] == self.state[l][1] == self.state[l][2]) & (self.state[l][0] != -1)
            if found:
                return found, self.state[l][0]

        # result diagonal
        found = (self.state[0][0] == self.state[1][1] == self.state[2][2]) & (self.state[0][0] != -1)
        if found:
            return found, self.state[0][0]
        found = (self.state[0][2] == self.state[1][1] == self.state[2][0]) & (self.state[0][2] != -1)
        if found:
            return found, self.state[0][2]

        # not found
        return False, -1

    def is_over(self, state):
        for l in state:
            for c in l:
                if c != -1: return False
        
        return True

    def generate_states(self, state, player):

        for l in range(len(state)):
            for c in range(len(state)):
                if state[l][c] != -1:
                    state[l][c] = player & 1 | 0

    #return 

if __name__ == "__main__":

    mode = input("Choose the game mode:\n"+
        "Player vs Machine(1) or  Machine vs Machine(0)")

    game = Game(mode)
    game.start()