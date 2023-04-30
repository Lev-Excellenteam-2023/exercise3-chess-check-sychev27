import unittest
from unittest.mock import Mock
import game_states_for_tests


my_knight1 = game_states_for_tests.my_knight1
my_knight2 = game_states_for_tests.my_knight2
my_knight3 = game_states_for_tests.my_knight3

my_game_state1 = game_states_for_tests.my_game_state1
my_game_state2 = game_states_for_tests.my_game_state2
my_game_state3 = game_states_for_tests.my_game_state3
my_game_state4 = game_states_for_tests.my_game_state4
my_game_state5 = game_states_for_tests.my_game_state5
my_game_state6 = game_states_for_tests.my_game_state6
my_game_state7 = game_states_for_tests.my_game_state7


class KnightTestCase(unittest.TestCase):
    my_mock = Mock()

    # Unit-test
    def test_get_valid_peaceful_moves(self):
        self.assertEqual(my_knight1.get_valid_peaceful_moves(my_game_state1), [(1, 3), (1, 5),
                                                                               (2, 2), (2, 6),
                                                                               (4, 2), (4, 6),
                                                                               (5, 5), (5, 3)])

        self.assertEqual(my_knight2.get_valid_peaceful_moves(my_game_state2), [(5, 1), (6, 2)])
        self.assertEqual(my_knight3.get_valid_peaceful_moves(my_game_state3), [(1, 6), (2, 5),
                                                                               (4, 5), (5, 6)])

    # Unit-test
    def test_get_valid_piece_takes(self):
        self.assertEqual(my_knight1.get_valid_piece_takes(my_game_state4), [])
        self.assertEqual(my_knight2.get_valid_piece_takes(my_game_state5), [(5, 1)])
        self.assertEqual(my_knight3.get_valid_piece_takes(my_game_state6), [(1, 6), (2, 5)])

    # Integration-test
    def test_get_valid_piece_moves(self):
        self.assertEqual(my_knight1.get_valid_piece_moves(my_game_state7), [(2, 6), (4, 6), (1, 3)])


if __name__ == '__main__':
    unittest.main()
