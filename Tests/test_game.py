import unittest
from chess_engine import game_state

my_game_state = game_state()


class GameTestCase(unittest.TestCase):
    # System-test
    def test_game(self):
        my_game_state.move_piece((1, 2), (2, 2), False)
        my_game_state.move_piece((6, 3), (4, 3), False)
        my_game_state.move_piece((1, 1), (3, 1), False)
        my_game_state.move_piece((7, 4), (3, 0), False)
        endgame = my_game_state.checkmate_stalemate_checker()
        # Check mate position
        self.assertEqual(endgame, 0)


if __name__ == '__main__':
    unittest.main()
