# Random module for randomly accepting the values
# ‘X’ indicates the ships hit
# ‘-‘ indicates the hits missed
from random import randint


class GameBoard:
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers(self):
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        print('  A B C D E')
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for ship in range(5):
            self.x_row, self.y_column = randint(0, 4), randint(0, 4)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = randint(0, 7), randint(0, 7)
                self.board[self.x_row][self.y_column] = "X"
            return self.board

    def get_user_input(self):
        # Enter the row number between 1 to 5
        try:
            x_row = input('Please enter a ship row 1-5 ').upper()
            while x_row not in '12345':
                print("Please enter a valid ship row ")
                x_row = input('Please enter a ship row 1-5 ')

        # Enter the Ship column from A TO H
            y_column = input('Please enter a ship column A-E ').upper()
            while y_column not in 'ABCDE':
                print("Please enter a valid column ")
                y_column = input('Please enter a ship column A-E ')
                return int(x_row)-1, \
                    GameBoard.get_letters_to_numbers(self)[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    def count_hit_ships(self):
        count = 0
        for row in self.board:
            for column in row:
                if column == 'X':
                    count += 1
        return count


def RunGame():
    computer_board = GameBoard([[" "] * 5 for i in range(5)])
    user_guess_board = GameBoard([[" "] * 5 for i in range(5)])
    Battleship.create_ships(computer_board)
    turns = 5
    while True:
        if turns >= 0:
            print('Welcome to Battleship')
            GameBoard.print_board(computer_board)
            user_x_row, user_y_column = Battleship.get_user_input(object)
            # check if duplicate guess
            while user_guess_board.board[user_x_row][user_y_column] == "-" or\
                    user_guess_board.board[user_x_row][user_y_column] == "X":
                print("You guessed that one already")
                user_x_row, user_y_column = Battleship.get_user_input(object)
            # check for hit or miss
            if computer_board.board[user_x_row][user_y_column] == "X":
                print("You sunk 1 of my battleship!")
                user_guess_board.board[user_x_row][user_y_column] = "X"
            else:
                print("You missed my battleship!")
                user_guess_board.board[user_x_row][user_y_column] = "-"
            # check for win or lose
            if Battleship.count_hit_ships(user_guess_board) == 5:
                print("You hit all 5 battleships!")
                break
            else:
                turns -= 1
                print(f"You have {turns} turns remaining")
            if turns == 0:
                print("Sorry you ran out of turns")
                GameBoard.print_board(user_guess_board)
                break


if __name__ == '__main__':
    RunGame()