import random

def rps_game():
    choices = ['rock', 'paper', 'scissors']
    p1 = random.choice(choices)
    p2 = random.choice(choices)
    if choices.index(p1) - choices.index(p2) == 1 or choices.index(p1) - choices.index(p2) == -2:
        return f'Player 1 wins! Player 1: {p1} vs. Player 2: {p2}'
    elif choices.index(p2) - choices.index(p1) == 1 or choices.index(p2) - choices.index(p1) == -2:
        return f'Player 2 wins! Player 1: {p1} vs. Player 2: {p2}'
    elif choices.index(p1) == choices.index(p2):
        return f'A draw! Player 1: {p1} vs. Player 2: {p2}'

print(rps_game())



choices = ['rock', 'paper', 'scissors']
p1 = random.choice(choices)
p2 = random.choice(choices)
if choices.index(p1) - choices.index(p2) == 1 or choices.index(p1) - choices.index(p2) == -2:
    print(f'Player 1 wins! Player 1: {p1} vs. Player 2: {p2}')
elif choices.index(p2) - choices.index(p1) == 1 or choices.index(p2) - choices.index(p1) == -2:
    print(f'Player 2 wins! Player 1: {p1} vs. Player 2: {p2}')
elif choices.index(p1) == choices.index(p2):
    print(f'A draw! Player 1: {p1} vs. Player 2: {p2}')



class GameClass():
    def __init__(self):
        choices = ['rock', 'paper', 'scissors']
        self.p1 = random.choice(choices)
        self.p2 = random.choice(choices)

    def game_simulation(self):
        return rps_game()

    def game_start(self, choice):
        pass

print(GameClass.game_simulation())
