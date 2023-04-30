from Piece import Rook, Knight, Bishop, Queen, King, Pawn
from chess_engine import game_state
from enums import Player

my_knight1 = Knight('n', 3, 4, Player.PLAYER_1)
my_knight2 = Knight('n', 7, 0, Player.PLAYER_1)
my_knight3 = Knight('n', 3, 7, Player.PLAYER_1)
my_rook1 = Rook('r', 1, 3, Player.PLAYER_1)
my_rook2 = Rook('r', 2, 2, Player.PLAYER_1)
my_rook3 = Rook('r', 5, 1, Player.PLAYER_2)
my_rook4 = Rook('r', 1, 3, Player.PLAYER_2)
my_bishop1 = Bishop('b', 1, 5, Player.PLAYER_1)
my_bishop2 = Bishop('b', 2, 6, Player.PLAYER_1)
my_bishop3 = Bishop('b', 1, 6, Player.PLAYER_2)
my_queen1 = Queen('q', 4, 2, Player.PLAYER_1)
my_queen2 = Queen('q', 5, 3, Player.PLAYER_1)
my_queen3 = Queen('q', 2, 5, Player.PLAYER_2)
my_pawn1 =Pawn('p', 5, 5, Player.PLAYER_1)
my_pawn2 =Pawn('p', 4, 6, Player.PLAYER_1)

my_game_state1 = game_state()
my_game_state2 = game_state()
my_game_state3 = game_state()
my_game_state4 = game_state()
my_game_state5 = game_state()
my_game_state6 = game_state()
my_game_state7 = game_state()

my_game_state1.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_knight1, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]

my_game_state2.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [my_knight2, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]

my_game_state3.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     my_knight3],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]

my_game_state4.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, my_rook1, Player.EMPTY, my_bishop1, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, my_rook2, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_bishop2,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_knight1, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, my_queen1, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_pawn2,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, my_queen2, Player.EMPTY, my_pawn1, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]

my_game_state5.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, my_rook3, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [my_knight2, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]

my_game_state6.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_bishop3,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_queen3, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     my_knight3],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]

my_game_state7.board = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, my_rook4, Player.EMPTY, my_bishop1, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, my_rook2, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, my_knight1, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, my_queen1, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, my_queen2, Player.EMPTY, my_pawn1, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
     Player.EMPTY]
]