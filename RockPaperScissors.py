# PROJECT حجرة ورقة مقص قمت بتسليمه
#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

# Base Player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# Human player input
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Choose: ROCK, PAPER, or SCISSORS? ")
            if move in moves:
                return move.lower()
            else:
                print("Invalid input. Please try again.")

# Always plays 'rock'
class RockPlayer(Player):
    def move(self):
        return 'rock'

# Chooses randomly each round
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# Copies opponent's last move( الاعب المنافس يختار نفس  الحركة السابقة)
class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = random.choice(moves)         #نجعل الاختيار السابق اختيار عشوائي

    def move(self):
        return self.their_last_move                         #رجع الحركة السابقة التي حصلت عليها

    def learn(self, my_move, their_move):
        self.their_last_move = their_move                   #نجعل الحركة الحالية تساوي الحركة السابقة

# Cycles through the moves (هنا المنافس يختار الخطوة الولى عشوائي لكن بعدها يتنقل عبر الحركات كلها بالترتيب بناءا على القائمة)
class CyclePlayer(Player):
    def __init__(self):
        self.last_move = random.choice(moves)

    def move(self):
        index = moves.index(self.last_move)    #لفحص موقع الحركة من قائمة الحركات
        next_move = moves[(index + 1) % len(moves)]   #الحركة الثانية تكون الحركة التالية في الترتيب في القائمة
        self.last_move = next_move                  #مع تكرار هنا اهمية %التي تعطي حركة تالية من البداية اذا كانت الحركة هي الاخيرةفي القائمة
        return next_move                      #بعد تسجيل الحركة السابقة في الذاكرة على انها التالية لاستخدامها تاليا نرجع الحركة التالية

    def learn(self, my_move, their_move):
        self.last_move = my_move

# Determines if one move beats another
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# Game class to manage gameplay
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  |  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins this round!\n")
            self.score_p1 += 1
        elif beats(move2, move1):
            print("Player 2 wins this round!\n")
            self.score_p2 += 1
        else:
            print("It's a tie!\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\nGame start!\n")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()

        print("\nFinal score:")
        print(f"Player 1: {self.score_p1}")
        print(f"Player 2: {self.score_p2}")
        if self.score_p1 > self.score_p2:
            print("The winner is Player 1!")
        elif self.score_p2 > self.score_p1:
            print("The winner is Player 2!")
        else:
            print("The game is a tie!")

# Allow user to choose which computer strategy to play against
def choose_opponent():
    print("Choose the computer player you want to play against:")
    print("1 - Rock Player (always plays rock)")
    print("2 - Random Player (chooses randomly)")
    print("3 - Reflect Player (copies your last move)")
    print("4 - Cycle Player (cycles through rock, paper, scissors)")

    while True:
        choice = input("Enter the number (1-4): ")
        if choice == '1':
            return RockPlayer()
        elif choice == '2':
            return RandomPlayer()
        elif choice == '3':
            return ReflectPlayer()
        elif choice == '4':
            return CyclePlayer()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Run the game
if __name__ == '__main__':
    opponent = choose_opponent()
    game = Game(HumanPlayer(), opponent)
    game.play_game()