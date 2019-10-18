#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer:
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer:
    def move(self):
        choice = ''
        while choice != 'rock' and choice != 'paper' and choice != 'scissors':
            choice = input("Pick: rock, paper, or scissors: ").lower()
            if choice == 'rock' or choice == 'paper' or choice == 'scissors':
                return choice

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer:
    def __init__(self):
        self.newmove = random.choice(moves)

    def move(self):
        return self.newmove

    def learn(self, my_move, their_move):
        self.newmove = their_move


class CyclePlayer:
    def __init__(self):
        self.newmove = random.choice(moves)

    def move(self):
        return self.newmove

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.newmove = 'paper'
        elif my_move == 'paper':
            self.newmove = 'scissors'
        else:
            self.newmove = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}\n")
        if beats(move1, move2):
            print("Player 1 gets a point!\n")
            self.p1score += 1
            print(f"P1: {self.p1score}\nP2: {self.p2score}\n")
        elif beats(move2, move1):
            print("Player 2 gets a point!\n")
            self.p2score += 1
            print(f"P1: {self.p1score}\nP2: {self.p2score}\n")
        else:
            print("TIE!\n")
            print(f"P1: {self.p1score}\nP2: {self.p2score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Let's play Rock, Paper, Scissors! 10 rounds total!")
        print("Game start!\n")
        for round in range(10):
            print(f"Round {round + 1}:")
            self.play_round()
        print(f"GAME OVER!\nTHE FINAL SCORE IS\n"
              f"PLAYER 1: {self.p1score}\nPLAYER 2: {self.p2score}\n")
        if self.p1score > self.p2score:
            print("PLAYER 1 WINS!")
        elif self.p1score < self.p2score:
            print("PLAYER 2 WINS!")
        else:
            print("IT'S A TIE GAME!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
