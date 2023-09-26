"""
Play Carrot Land!
You have been sowing seeds to grow carrots in your garden.
But a rowdy rabbit is picking the carrots from underground
leaving nothing but the leaves left.
When it's time for you to harvest you see the leaves,
but not if there is a carrot attached.
Try to find the carrots that are left, but you have to hurry!
 You only have 10 tries and there is only 5 carrots left!

X = Found a carrot!
- = Only leave!
Good Luck!
"""
from random import randint


class Board:
    def __init__(self, board):
        self.board = board

    def letters_to_numbers(self):
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        print('  A B C D E')
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class Carrots:
    def __init__(self, board):
        self.board = board

    def create_carrots(self):
        for carrot in range(5):
            carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            while self.board[carrot_r][carrot_cl] == 'X':
                carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            self.board[carrot_r][carrot_cl] = 'X'

    def get_user_input(self):
        try:
            x_row = input("Look for carrot on row(1-5)...: ")
            while x_row not in '12345':
                print('Not valid! Select a valid row(1-5).')
                x_row = input("Look for carrot on row(1-5)...: ")
            y_column = input("Choose a column(A-E): ").upper()
            while y_column not in "ABCDE":
                print('Not valid! Select a valid column(A-E).')
                y_column = input("Choose a column(A-E): ").upper()
            return int(x_row) - 1, \
                Board.letters_to_numbers(self)[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    def find_carrots(self):
        find_carrots = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    find_carrots += 1
        return find_carrots


def GameOver():
    allowed_inputs = "yYnN"
    user_input = input("Play again (Y/N)? ")
    if user_input == "Y" or user_input == "y":
        Play_Game()
    if user_input == "N" or user_input == "n":
        print("Thank you for playing!")
        exit()


def Play_Game():
    print('''
========================================================================
                        Welcome to Carrotland!
The rowdy rabbit has almost taken all of the carrots from the garden from
underground. He left the leaves sticking up so you don't know if there is
a carrot attached to it.
There are 5 carrots left! Find them before the rowdy rabbit does!

        X = Found a carrot!
        - = Only leaves!
                            Good Luck!
======================================================================
''')
    computer_board = Board([[" "] * 5 for i in range(5)])
    user_guess_board = Board([[" "] * 5 for i in range(5)])
    Carrots.create_carrots(computer_board)
    # start 10 turns
    turns = 25
    while turns > 0:
        Board.print_board(user_guess_board)
        # get user input
        user_x_row, user_y_column = Carrots.get_user_input(object)
        # check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "-"\
                or user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You searched there already")
            user_x_row, user_y_column = Carrots.get_user_input(object)
            # check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("YEAH! You found a carrot!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("Sorry! No carrot!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
            # check for win or lose
        if Carrots.find_carrots(user_guess_board) == 5:
            print("CONGRATULATION! You found all 5 carrots! Yum! carrotcake!")
            GameOver()
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print('Game Over ')
                GameOver()


if __name__ == '__main__':
    Play_Game()