import math
import time
from player import HumanPlayer, ComputerPlayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_game_board_help():
        print('Here is our little guidance, the game board looks like this:')
        number_board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def winner(self, square, symbol):
        row_index = math.floor(square / 3)
        row = self.board[row_index * 3:(row_index + 1) * 3]
        if all([s == symbol for s in row]):
            return True

        col_index = square % 3
        col = [self.board[col_index + i * 3] for i in range(3)]
        if all([s == symbol for s in col]):
            return True

        if square % 2 == 0:
            dia_falling = [self.board[i] for i in [0, 4, 8]]
            if all([s == symbol for s in dia_falling]):
                return True
            dia_rising = [self.board[i] for i in [2, 4, 6]]
            if all([s == symbol for s in dia_rising]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, square in enumerate(self.board) if square == " "]


def play(game, player_x, player_o, print_game=True):
    if print_game:
        game.print_game_board_help()

    symbol = 'X'
    while game.empty_squares():
        if symbol == 'O':
            square = player_o.get_move(game)
        else:
            square = player_x.get_move(game)

        if game.make_move(square, symbol):
            if print_game:
                print(symbol + ' makes a move to square {}'.format(square))
                game.print_board()

            if game.current_winner:
                if print_game:
                    print(symbol + ' wins!')
                return symbol

            if symbol == 'X':
                symbol = 'O'
            else:
                symbol = 'X'

        time.sleep(0.5)

    if print_game:
        print('It\'s a tie.')


if __name__ == '__main__':
    # A little test to see that the smart Computer never loses:
    # Tip: Comment out the time.sleep(0.5) line to reduce waiting time
    #
    # x_wins = 0
    # o_wins = 0
    # ties = 0
    # for i in range(500):
    #    print(i)
    #    x_player = SmartComputerPlayer('X')
    #    o_player = ComputerPlayer('O')
    #    t = TicTacToe()
    #    symbol = play(t, x_player, o_player, print_game=False)
    #    if symbol == 'X':
    #        x_wins += 1
    #    elif symbol == 'O':
    #        o_wins += 1
    #    else:
    #        ties += 1
    # print('As you can see the smart computer never lost, with {} wins, {} ties, and {} losses.'.format(x_wins, ties,
    #                                                                                                   o_wins))

    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
