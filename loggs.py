import logging
from enums import Player

logging.basicConfig(filename="log_test.log", level=logging.DEBUG)
logger = logging.getLogger()


def log_for_current_pieces(game_state):
    names_of_black_pieces = []
    names_of_white_pieces = []
    board = game_state.board
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] != Player.EMPTY:
                if board[row][col].get_player() == Player.PLAYER_1:
                    names_of_white_pieces.append(board[row][col].get_name())
                else:
                    names_of_black_pieces.append(board[row][col].get_name())

    logger.debug("\nCurrent white pieces on the board are " + str(names_of_white_pieces) + "\n"
                 "Current black pieces on the board are " + str(names_of_black_pieces) + "\n")


def log_for_knight_move(moving_piece, num_of_white_knight_move, num_of_black_knight_move):
    new_num_of_white_knight_move = num_of_white_knight_move
    new_num_of_black_knight_move = num_of_black_knight_move
    if moving_piece.get_name() == "n":
        if moving_piece.get_player() == Player.PLAYER_1:
            new_num_of_white_knight_move += 1
            logger.debug("White knight made a move " + str(new_num_of_white_knight_move))
        else:
            new_num_of_black_knight_move += 1
            logger.debug("Black knight made a move " + str(new_num_of_black_knight_move))
    return new_num_of_white_knight_move, new_num_of_black_knight_move


def log_for_winner(endgame_code):
    if endgame_code == 0:
        logger.debug("Black wins.")
    elif endgame_code == 1:
        logger.debug("White wins.")
    elif endgame_code == 2:
        logger.debug("Stalemate.")


def log_for_who_started(num_of_players,human_player):
    if num_of_players == 2:
        logger.debug("2 human players and white player began\n")
    elif human_player == 'w':
        logger.debug("human player is white and he began\n")
    else:
        logger.debug("human player is black and white computer player began\n")


def log_of_game_begining():
    logger.info("\n--------Next game----------\n")