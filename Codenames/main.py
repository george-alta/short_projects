from data import WORDLIST
import random
from board import CodenamesBoard


random.shuffle(WORDLIST)
board = CodenamesBoard(WORDLIST, num_agents=2)
board.display_board()

print(board.assignments)

while True:
    guess = input("select a word: ")
    board.reveal_word(guess)
    board.display_board

# TODO game dynamics
