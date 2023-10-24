import random
from data import WORDLIST
import tkinter as tk
# comment


class CodenamesBoard:
    def __init__(self, game_words, num_agents=2):
        """
        Initialize a Codenames board.

        Args:
        - words (list): List of words for the game.
        - num_agents (int): Number of teams (default is 2).
        """
        # self.game_words = game_words
        self.board_words = game_words[:25]
        self.num_agents = num_agents
        self.grid = []
        self.assignments = {}
        self.create_board()
        self.team_1_words = []
        self.team_2_words = []
        self.assassin = []

    def create_board(self):
        """
        Create a random 5x5 grid of words from the word list.
        """
        print(self.board_words)
        random.shuffle(self.board_words)
        self.team_1_words = self.board_words[0:5]
        print(f"team 1 : {self.team_1_words}")
        self.team_2_words = self.board_words[5:10]
        print(f"team 2 : {self.team_2_words}")
        self.assassin = self.board_words[10]
        print(f"assassin: {self.assassin}")
        random.shuffle(self.board_words)
        self.grid = [self.board_words[i:i +
                                      5] for i in range(0, 25, 5)]

        self.assignments = {
            'Team 1': self.team_1_words,
            'Team 2': self.team_2_words,
            'Assassin': self.assassin
        }

    def display_board(self):
        """
        Display the Codenames board.
        """
        for row in self.grid:
            formatted_row = " | ".join(word.center(20)[:20] for word in row)
            print(formatted_row)

    def reveal_word(self, word):
        """
        Reveal a word on the board and return its assignment.

        Args:
        - word (str): The word to reveal.

        Returns:
        - str: The assignment of the revealed word.
        """
        for team, words in self.assignments.items():
            if word in words:
                print(team)
                return team
        print("neutral")
        return "Neutral"


root = tk.Tk()
root.title("Codenames Board")

# Create a CodenamesBoard instance
board = CodenamesBoard(WORDLIST, num_agents=2)
board.display_board()
# Function to update the label text when a word is revealed


def reveal_word(word, label):
    assignment = board.reveal_word(word)
    label.config(text=word, bg='white', fg='red' if assignment ==
                 'Team 1' else 'blue' if assignment == 'Team 2' else 'black')


# Create a 5x5 grid of labels to display the board
labels = [[None for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        word = board.grid[i][j]
        label = tk.Label(root, text=word, width=20, height=3, relief="ridge")
        label.grid(row=i, column=j)
        labels[i][j] = label

        # Bind a click event to each label to reveal the word
        label.bind("<Button-1>", lambda event, word=word,
                   label=label: reveal_word(word, label))

# Start the Tkinter main loop
root.mainloop()
