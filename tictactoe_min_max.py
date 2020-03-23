#mim max algorithm to solve tictactoe
#Author Vinicius Franca

#https://www.geeksforgeeks.org/python-gui-tkinter/
#http://www.codekraft.co/freecodecamp/jogo-da-velha-entendendo-o-algoritimo-minimax/
import random
import copy
import sys

sys.setrecursionlimit(3000)

class Game:
    def __init__(self, mode):
        self.state = [[]]
        self.mode = mode
        self.player = True #true for p1 and false for p3

    def start(self):
        self.state = [[-1 for i in range(0, 3)] for c in range(0, 3)]
        self.pass_turn()

    def show(self):
        for l in self.state:
            print(l)
        print('')

    def pass_turn(self):
        result = self.winner(self.state)
        if result[0] | self.is_over(self.state):
            print('*************************')
            print('The Game is over')
            if result[1] != -1: 
                print('The Winner is Player {}'.format(result[1]))
            else:
                print('O jogo empatou')
            self.show()
            print('*************************')
            return 

        if (mode == 1) & (not (self.player)):
            l = input('\n*Insira a linha 1 a 3: ')
            c = input('\n*Insira a coluna 1 a 3: ')
            self.state[l-1][c-1] = 0
        
        self.show()
        self.generate_states(self.state, self.player, 0)
        self.player = not self.player
        self.pass_turn()
    
    def winner(self, state):
        # result linha
        for l in state:
            found = (l[0] == l[1] == l[2]) & (l[0] != -1)
            if found: 
                return found, l[0]

        # result column
        for l in range(len(state)):
            found = (state[l][0] == state[l][1] == state[l][2]) & (state[l][0] != -1)
            if found:
                return found, state[l][0]

        # result diagonal
        found = (state[0][0] == state[1][1] == state[2][2]) & (state[0][0] != -1)
        if found:
            return found, state[0][0]
        found = (state[0][2] == state[1][1] == state[2][0]) & (state[0][2] != -1)
        if found:
            return found, state[0][2]

        # not found
        return False, -1

    def generate_states(self, state, player, height):
        draw_choices = []
        win_choices = []
        if(not (self.is_over(state))):
            result = self.winner(state)
            if(result[0] & (result[1]==0)):
                return -10
            elif(result[0] & (result[1]==1)):
                return 10
            for choice in self.choices(state, player):
                value = self.generate_states(choice, not player, height+1)
                if (((value == 10) & player) | ((value == -10) & (not player))):
                    win_choices.append({'value': value, 'state': choice})
                elif (value == 0):
                    draw_choices.append({'value': value, 'state': choice})
                
            if len(win_choices) > 0:
                rand_choice = random.randint(0, (len(win_choices))-1)
                temp_choice = win_choices[rand_choice]
                if height == 0: self.state = copy.deepcopy(temp_choice['state'])
                return temp_choice['value']
            elif len(draw_choices) > 0:
                rand_choice = random.randint(0, (len(draw_choices))-1)
                temp_choice = draw_choices[rand_choice]
                if height == 0: self.state = copy.deepcopy(temp_choice['state'])
                return temp_choice['value']
            else:
                return ((player & -10) | 10)
        

        result = self.winner(state)
        if(result[0] & (result[1]==0)):
            return -10
        elif(result[0] & (result[1]==1)):
            return 10
        else:
            return 0

    def is_over(self, state):
        for l in range(len(state)):
            for c in range(len(state)):
                if state[l][c] == -1:
                    return False
        return True

    def choices(self, state, player):
        choices = []
        for l in range(len(state)):
            for c in range(len(state)):
                if state[l][c] == -1:
                    temp_state = copy.deepcopy(state)
                    temp_state[l][c] = (player & 1) | 0
                    choices.append(copy.deepcopy(temp_state))
                    del temp_state
        return choices

if __name__ == "__main__":

    mode = input("Choose the game mode:\n"+
        "Player vs Machine(1) or  Machine vs Machine(0)")

    game = Game(mode)
    game.start()