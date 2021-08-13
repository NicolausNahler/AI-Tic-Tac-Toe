import math
import random


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        valid_square = False
        index = None
        while not valid_square:
            square = input(self.symbol + '\'s turn. Input move (0-8): ')

            try:
                index = int(square)
            except ValueError:
                print('Invalid square. You did not use a number. Try again with a number from 0-8.')
                continue

            if index > 8 or index < 0:
                print('Invalid square. You did not use a number from 0-8. Try again with a number from 0-8.')
                continue

            if 0 <= index <= 8 and index not in game.available_moves():
                print('Square has already been used. Try again.')
                continue

            valid_square = True
        return index


class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.best_move(game, self.symbol)['position']
        return square

    def best_move(self, state, player):
        max_player = self.symbol
        min_player = 'O' if player == 'X' else 'X'

        if state.current_winner:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if min_player == max_player else -1 * (
                            state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim = self.best_move(state, min_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim['position'] = possible_move

            if player == max_player:
                if sim['score'] > best['score']:
                    best = sim
            else:
                if sim['score'] < best['score']:
                    best = sim
        return best
