from moveGenerator import MoveGenerator
from chessBitBoard import Bitboard
from src.ia.move import Move


class BitBoardMoveGenerator:
    moveGenerator: MoveGenerator
    coloredPieces: dict[bool, str]

    def __init__(self):
        self.moveGenerator = MoveGenerator()
        self.coloredPieces = {
            True: 'PNBRQK',
            False: 'pnbrqk'
        }

    def gen_bishop_moves(self, board: Bitboard, us: bool) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[us]
        them_pieces = board.side_pieces[not us]
        return self.moveGenerator.gen_bishop_move(board.pieces[us_pieces_list[2]], us_pieces,
                                                  board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                  board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                  board.pieces[them_pieces_list[4]], them_pieces, board.occupancy)

    def gen_rook_moves(self, board: Bitboard, us: bool) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[us]
        them_pieces = board.side_pieces[not us]
        return self.moveGenerator.gen_rook_move(board.pieces[us_pieces_list[3]], us_pieces,
                                                board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                board.pieces[them_pieces_list[4]], them_pieces, board.occupancy)

    def gen_queen_moves(self, board: Bitboard, us: bool) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[us]
        them_pieces = board.side_pieces[not us]
        return self.moveGenerator.gen_queen_move(board.pieces[us_pieces_list[4]], us_pieces,
                                                 board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                 board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                 board.pieces[them_pieces_list[4]], them_pieces, board.occupancy)

    def gen_knight_moves(self, board: Bitboard, us: bool) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[us]
        them_pieces = board.side_pieces[not us]
        return self.moveGenerator.gen_knight_moves(board.pieces[us_pieces_list[1]], us_pieces,
                                                   board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                   board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                   board.pieces[them_pieces_list[4]], them_pieces)

    def gen_king_moves(self, board: Bitboard, us: bool) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[us]
        them_pieces = board.side_pieces[not us]
        return self.moveGenerator.gen_king_moves(board.pieces[us_pieces_list[5]], us_pieces,
                                                 board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                 board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                 board.pieces[them_pieces_list[4]], them_pieces)

    def gen_pawn_moves(self, board: Bitboard, us: bool) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[us]
        them_pieces = board.side_pieces[not us]
        return self.moveGenerator.gen_pawn_moves(board.pieces[us_pieces_list[0]], us, us_pieces,
                                                 board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                 board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                 board.pieces[them_pieces_list[4]], them_pieces)
