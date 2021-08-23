from chessBitBoard import Bitboard
from zobrist import ZobristInformations


class ZobristBoard:
    board: Bitboard
    current_hash: int

    def __init__(self, fen: str):
        self.board = Bitboard(fen)
        self.current_hash = zobrist_from_board(self.board).__hash__()


def zobrist_from_board(board: Bitboard) -> ZobristInformations:
    return ZobristInformations(board.pieces['P'], board.pieces['p'], board.pieces['N'], board.pieces['n'],
                               board.pieces['B'], board.pieces['b'], board.pieces['R'], board.pieces['r'],
                               board.pieces['Q'], board.pieces['q'], board.pieces['K'], board.pieces['k'],
                               board.board_info.us, board.board_info.can_white_king_side_castle,
                               board.board_info.can_white_queen_side_castle,
                               board.board_info.can_black_king_side_castle,
                               board.board_info.can_black_queen_side_castle,
                               board.board_info.can_en_passant, board.board_info.en_passant_sqr)
