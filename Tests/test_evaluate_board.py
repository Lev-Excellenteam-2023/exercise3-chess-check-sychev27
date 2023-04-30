import unittest

from ai_engine import chess_ai
from enums import Player
import game_states_for_tests

my_chess_ai = chess_ai()
my_game_state1= game_states_for_tests.my_game_state7
my_game_state2 = game_states_for_tests.my_game_state6


class EvaluateBoardTestCase(unittest.TestCase):
    # Integration-test
    def test_evaluate_board(self):
        self.assertEqual(chess_ai.evaluate_board(my_chess_ai, my_game_state1, Player.PLAYER_1), -270)
        self.assertEqual(chess_ai.evaluate_board(my_chess_ai, my_game_state2, Player.PLAYER_1), 100)


if __name__ == '__main__':
    unittest.main()
