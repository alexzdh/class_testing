import random

def rps_game():
    choices = ['rock', 'paper', 'scissors']
    p1 = random.choice(choices)
    p2 = random.choice(choices)
    p1_index = choices.index(p1)
    p2_index = choices.index(p2)

    if p1_index - p2_index == 1 or p1_index - p2_index == -2:
        return f'Player 1 wins! Player 1: {p1}, vs. Player 2: {p2}.'
    elif p2_index - p1_index == 1 or p2_index - p1_index == -2:
        return f'Player 2 wins! Player 1: {p1}, vs. Player 2: {p2}.'
    elif p1_index == p2_index:
        return f'A draw! Player 1: {p1}, vs. Player 2: {p2}.'

print(rps_game())



choices = ['rock', 'paper', 'scissors']
p1 = random.choice(choices)
p2 = random.choice(choices)
if choices.index(p1) - choices.index(p2) == 1 or choices.index(p1) - choices.index(p2) == -2:
    print(f'Player 1 wins! Player 1: {p1}, vs. Player 2: {p2}')
elif choices.index(p2) - choices.index(p1) == 1 or choices.index(p2) - choices.index(p1) == -2:
    print(f'Player 2 wins! Player 1: {p1}, vs. Player 2: {p2}')
elif choices.index(p1) == choices.index(p2):
    print(f'A draw! Player 1: {p1}, vs. Player 2: {p2}')



class GameClass():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.p1 = random.choice(choices)
        self.p2 = random.choice(choices)

    def game_simulation(self):
        return rps_game()

    def game_start(self, strat):
        self.strat = strat
        player_index = self.choices.index(self.strat)
        p1_index = self.choices.index(self.p1)

        if player_index - p1_index == 1 or player_index - p1_index == -2:
            return f'You win! You: {self.strat}, vs. Computer: {self.p1}.'
        elif p1_index - player_index == 1 or p1_index - player_index == -2:
            return f'You lose! You: {self.strat}, vs. Computer: {self.p1}.'
        elif player_index == p1_index:
            return f'A draw! You: {self.strat}, vs. Computer: {self.p1}.'


rps_instance = GameClass()
print(rps_instance.game_simulation())
print(rps_instance.game_start('rock'))
