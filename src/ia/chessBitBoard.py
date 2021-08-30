from __future__ import annotations
from bit_utils import extract_index
from move import Move
from boardInfo import BoardInfo
import CONSTANTS
from collections import deque
from copy import copy
from moveGenerator import MoveGenerator, MOVE_GENERATOR


class BitBoardMoveGenerator:
    moveGenerator: MoveGenerator
    coloredPieces: dict[bool, str]

    def __init__(self):
        self.moveGenerator = MOVE_GENERATOR
        self.coloredPieces = {
            True: 'PNBRQK',
            False: 'pnbrqk'
        }

    def gen_attacks(self, board: Bitboard, side: bool) -> int:
        side_pieces_list = list(self.coloredPieces[side])
        return self.moveGenerator.gen_attacks(side, board.pieces[side_pieces_list[0]],
                                              board.pieces[side_pieces_list[1]],
                                              board.pieces[side_pieces_list[2]], board.pieces[side_pieces_list[3]],
                                              board.pieces[side_pieces_list[4]], board.pieces[side_pieces_list[5]],
                                              board.occupancy)

    def gen_moves(self, board: Bitboard) -> list[Move]:
        result = []
        result += self.gen_pawn_moves(board)
        result += self.gen_knight_moves(board)
        result += self.gen_bishop_moves(board)
        result += self.gen_queen_moves(board)
        result += self.gen_king_moves(board)
        result += self.gen_rook_moves(board)
        return result

    def gen_legal_moves(self, board: Bitboard):
        # DO NOT USE THIS METHOD WHILE SEARCHING
        result = []
        moves = self.gen_moves(board)
        for move in moves:
            if board.make_move(move):
                result.append(move)
                board.unmake_move()
        return result

    def gen_bishop_moves(self, board) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[board.board_info.us])
        them_pieces_list = list(self.coloredPieces[not board.board_info.us])
        us_pieces = board.side_pieces[board.board_info.us]
        them_pieces = board.side_pieces[not board.board_info.us]
        return self.moveGenerator.gen_bishop_move(board.pieces[us_pieces_list[2]], us_pieces,
                                                  board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                  board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                  board.pieces[them_pieces_list[4]], them_pieces, board.occupancy)

    def gen_rook_moves(self, board) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[board.board_info.us])
        them_pieces_list = list(self.coloredPieces[not board.board_info.us])
        us_pieces = board.side_pieces[board.board_info.us]
        them_pieces = board.side_pieces[not board.board_info.us]
        return self.moveGenerator.gen_rook_move(board.pieces[us_pieces_list[3]], us_pieces,
                                                board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                board.pieces[them_pieces_list[4]], them_pieces, board.occupancy)

    def gen_queen_moves(self, board) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[board.board_info.us])
        them_pieces_list = list(self.coloredPieces[not board.board_info.us])
        us_pieces = board.side_pieces[board.board_info.us]
        them_pieces = board.side_pieces[not board.board_info.us]
        return self.moveGenerator.gen_queen_move(board.pieces[us_pieces_list[4]], us_pieces,
                                                 board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                 board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                 board.pieces[them_pieces_list[4]], them_pieces, board.occupancy)

    def gen_knight_moves(self, board) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[board.board_info.us])
        them_pieces_list = list(self.coloredPieces[not board.board_info.us])
        us_pieces = board.side_pieces[board.board_info.us]
        them_pieces = board.side_pieces[not board.board_info.us]
        return self.moveGenerator.gen_knight_moves(board.pieces[us_pieces_list[1]], us_pieces,
                                                   board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                   board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                   board.pieces[them_pieces_list[4]], them_pieces)

    def gen_king_moves(self, board) -> list[Move]:
        result = []
        us = board.board_info.us
        us_pieces_list = list(self.coloredPieces[us])
        them_pieces_list = list(self.coloredPieces[not us])
        us_pieces = board.side_pieces[board.board_info.us]
        them_pieces = board.side_pieces[not board.board_info.us]
        can_queen_side_castle = board.board_info.can_white_queen_side_castle if us else board.board_info.can_black_queen_side_castle
        can_king_side_castle = board.board_info.can_white_king_side_castle if us else board.board_info.can_black_king_side_castle
        result += self.moveGenerator.gen_king_moves(board.pieces[us_pieces_list[5]], us_pieces,
                                                    board.pieces[them_pieces_list[0]],
                                                    board.pieces[them_pieces_list[1]],
                                                    board.pieces[them_pieces_list[2]],
                                                    board.pieces[them_pieces_list[3]],
                                                    board.pieces[them_pieces_list[4]], them_pieces)
        result += self.moveGenerator.gen_castle_moves(board.board_info.us, board.pieces[us_pieces_list[5]],
                                                      board.occupancy, can_king_side_castle, can_queen_side_castle,
                                                      board.moveGenerator.gen_attacks(board, not us))
        return result

    def gen_pawn_moves(self, board) -> list[Move]:
        us_pieces_list = list(self.coloredPieces[board.board_info.us])
        them_pieces_list = list(self.coloredPieces[not board.board_info.us])
        us_pieces = board.side_pieces[board.board_info.us]
        them_pieces = board.side_pieces[not board.board_info.us]
        return self.moveGenerator.gen_pawn_moves(board.pieces[us_pieces_list[0]], board.board_info.us, us_pieces,
                                                 board.pieces[them_pieces_list[0]], board.pieces[them_pieces_list[1]],
                                                 board.pieces[them_pieces_list[2]], board.pieces[them_pieces_list[3]],
                                                 board.pieces[them_pieces_list[4]], them_pieces, board.occupancy,
                                                 board.board_info.can_en_passant, board.board_info.en_passant_sqr)


# IMPORTANT NOTE : Although we're using ints everywhere, there are different kind of them : int representing squares
# are 0 to 63. int representing bitboards are 0 to 2 ^ 64 - 1, ints representing bitboards hashes vary in size but
# are maximum 2^12 - 1
class Bitboard:
    pieces: dict[str, int]
    side_pieces: dict[bool, int]
    occupancy: int
    moves: deque[Move]
    prev_board_infos: deque[BoardInfo]
    board_info: BoardInfo
    moveGenerator: BitBoardMoveGenerator
    
    # dict[etat(checkmate or not), couleur(w = true, b = false)]
    check_mate: dict[bool, bool]
    # dict[etat(couleur(w = true, b = false), king in check or not]
    king_check: dict[bool, bool]

    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        self.moves = deque()
        self.prev_board_infos = deque()
        self.board_info = BoardInfo(False, 0, False, False, False, False, 0, True)
        self.moveGenerator = BitBoardMoveGenerator()
        self.king_check = {True: False, False: False}

        # Pieces bitboard dictionnary
        self.pieces = {
            'r': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'n': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'b': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'q': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'k': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'p': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'R': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'N': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'B': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'Q': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'K': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'P': 0b0000000000000000000000000000000000000000000000000000000000000000,
        }

        # Fill the bitboard dictionnary
        i = 64
        groups = fen.split(' ')
        rev = groups[0].split('/')
        res = []
        for r in rev:
            res.append(r[::-1])
        rev = '/'.join(res)
        for p in rev:
            i -= 1 if ord(p) > 57 else ord(p) - 48 if ord(p) > 47 else 0
            if i < 0 or p not in self.pieces:
                continue
            self.pieces[p] += 2 ** i

        if groups[1] == 'w':
            self.board_info.us = True
        else:
            self.board_info.us = False

        if 'K' in groups[2]:
            self.board_info.can_white_king_side_castle = True
        if 'Q' in groups[2]:
            self.board_info.can_white_queen_side_castle = True
        if 'k' in groups[2]:
            self.board_info.can_black_king_side_castle = True
        if 'q' in groups[2]:
            self.board_info.can_black_queen_side_castle = True

        self.side_pieces = dict()
        self.side_pieces[True] = self.get_white_pieces()
        self.side_pieces[False] = self.get_black_pieces()
        self.occupancy = self.get_occupancy()

    def __str__(self):
        line_list = []
        result = ''
        for i in range(8):
            line_list.append([])
            for j in range(8):
                line_list[i].append(' ')
        for i in 'rnbqkpRNBQKP':
            for index in extract_index(self.pieces[i]):
                line_list[index // 8][index % 8] = i
        line_list.reverse()
        for i in range(8):
            result += '|' + '|'.join(line_list[i]) + '|\n'
        return result

    # Retrieve FEN line from dictionnary
    def get_fen(self):
        fen = ""
        line = ""
        tmp = 0 # represents blank squares
        for i in range(0, 64):
            found = False
            if i > 0 and i % 8 == 0:
                # if EOL and tmp > 0, append it
                if tmp > 0:
                    line = str(tmp) + line
                    tmp = 0
                fen += line
                fen += '/'
                line = ""

            for key, value in self.pieces.items():
                value = list(f'{value:064b}')
                if value[i] == '1':
                    if tmp > 0:
                        line = str(tmp) + line
                        tmp = 0
                    line = key + line
                    found = True
                    break
            if not found:
                tmp += 1

            if i == 63:
                line = str(tmp) + line
                fen += line

        if self.board_info.us:
            fen += ' w '
        else:
            fen += ' b '

        anyCastle = False
        if self.board_info.can_white_king_side_castle:
            anyCastle = True
            fen += 'K'
        if self.board_info.can_white_queen_side_castle:
            anyCastle = True
            fen += 'Q'
        if self.board_info.can_black_king_side_castle:
            anyCastle = True
            fen += 'k'
        if self.board_info.can_black_queen_side_castle:
            anyCastle = True
            fen += 'q'
        if not anyCastle:
            fen += '-'

        if self.board_info.can_en_passant:
            index_to_line = ['1', '2', '3', '4', '5', '6', '7', '8']
            index_to_column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            line = self.board_info.en_passant_sqr // 8
            col = self.board_info.en_passant_sqr % 8
            fen += f' {index_to_column[col] + index_to_line[line]}'
        else:
            fen += ' -'
        fen += f' {self.board_info.half_move_clock} {(len(self.moves))//2}'
        return fen

    def get_us_pieces(self, us):
        if us:
            return self.get_white_pieces()
        else:
            return self.get_black_pieces()

    def get_white_pieces(self):
        white_pieces = 0
        for s in 'RNBKQP':
            white_pieces |= self.pieces[s]
        return white_pieces

    def get_black_pieces(self):
        black_pieces = 0
        for s in 'rnbqkp':
            black_pieces |= self.pieces[s]
        return black_pieces

    def get_occupancy(self):
        return self.side_pieces[True] | self.side_pieces[False]

    # Get piece type from bitboard index
    def get_piece_by_index(self, index):
        for key, value in self.pieces.items():
            if value & (2 ** index) > 0:
                return key
        return 'None'

    def move_piece(self, start: int, end: int, us: bool, piece_type: int):
        self.pieces[CONSTANTS.COLORED_PIECES[us][piece_type - 1]] ^= 0b1 << start
        self.pieces[CONSTANTS.COLORED_PIECES[us][piece_type - 1]] ^= 0b1 << end

    def make_move(self, move: Move) -> bool:
        # Updating move and state history stacks
        self.moves.append(move)
        self.prev_board_infos.append(copy(self.board_info))
        # Declaring turn based variables
        us = self.board_info.us
        them = not self.board_info.us
        # Moving the piece
        self.move_piece(move.start, move.end, us, move.pieceType)
        if move.moveType == 1:
            self.pieces[CONSTANTS.COLORED_PIECES[them][move.capturedPieceType - 1]] &= ~ (0b1 << move.end)
        if move.specialMoveFlag > 0:
            # Case en passant capture
            if move.specialMoveFlag == 1:
                if us:
                    self.pieces['p'] ^= 1 << (self.board_info.en_passant_sqr - 8)
                else:
                    self.pieces['P'] ^= 1 << (self.board_info.en_passant_sqr + 8)
            # Case castling
            if move.specialMoveFlag == 2:
                # Moving the rook (king already moved)
                if us:
                    if move.castleSide:
                        self.move_piece(7, 5, us, 4)
                    else:
                        self.move_piece(0, 3, us, 4)
                else:
                    if move.castleSide:
                        self.move_piece(63, 61, us, 4)
                    else:
                        self.move_piece(56, 59, us, 4)
            # Case promotion
            if move.specialMoveFlag == 3:
                self.pieces[CONSTANTS.COLORED_PIECES[us][0]] ^= 0b1 << move.end
                self.pieces[CONSTANTS.COLORED_PIECES[us][move.promotionPieceType - 1]] ^= 0b1 << move.end
            # Case double pawn push
            if move.specialMoveFlag == 4:
                self.board_info.can_en_passant = True
                self.board_info.en_passant_sqr = move.start + 8 if us else move.start - 8
        # Updating the half-move clock:
        if move.moveType == 1 or move.pieceType == 1:
            self.board_info.half_move_clock = 0
        else:
            self.board_info.half_move_clock += 1
        # Updating en passant status if the move is not a double pawn push
        if not move.specialMoveFlag == 4:
            self.board_info.can_en_passant = False
        # Updating castling rights
        if move.pieceType == 6:
            if us:
                self.board_info.can_white_queen_side_castle = False
                self.board_info.can_white_king_side_castle = False
            else:
                self.board_info.can_black_king_side_castle = False
                self.board_info.can_black_queen_side_castle = False
        if move.pieceType == 4:
            if us:
                if self.pieces['R'] & 1 == 0:
                    self.board_info.can_white_queen_side_castle = False
                if self.pieces['R'] & 1 << 7 == 0:
                    self.board_info.can_white_king_side_castle = False
            else:
                if self.pieces['r'] & 1 << 56 == 0:
                    self.board_info.can_black_queen_side_castle = False
                if self.pieces['r'] & 1 << 63 == 0:
                    self.board_info.can_black_king_side_castle = False
        # Updating board properties
        self.side_pieces[us] = self.get_us_pieces(us)
        self.side_pieces[them] = self.get_us_pieces(them)
        self.occupancy = self.get_occupancy()
        # Updating who's turn to move it is
        self.board_info.us = not self.board_info.us
        # Checking that the board is legal and unmaking if it isn't
        them_attacks = self.moveGenerator.gen_attacks(self, them)
        if them_attacks & self.pieces[CONSTANTS.COLORED_PIECES[us][5]] > 0:
            self.unmake_move()
            return False
        return True

    def unmove_piece(self, start, end, us, piece_type):
        self.pieces[CONSTANTS.COLORED_PIECES[us][piece_type - 1]] &= ~ (0b1 << end)
        self.pieces[CONSTANTS.COLORED_PIECES[us][piece_type - 1]] |= 0b1 << start

    def create_piece(self, square, piece_type, color):
        self.pieces[CONSTANTS.COLORED_PIECES[color][piece_type - 1]] |= 1 << square

    def unmake_move(self):
        move = self.moves.pop()
        board_info = self.prev_board_infos.pop()
        self.board_info = board_info
        us = self.board_info.us
        them = not self.board_info.us
        self.unmove_piece(move.start, move.end, us, move.pieceType)
        if (move.specialMoveFlag == 0 or move.specialMoveFlag == 3) and move.moveType == 1:
            self.create_piece(move.end, move.capturedPieceType, them)
        # Case en passant
        if move.specialMoveFlag == 1:
            if us:
                self.create_piece(move.end - 8, 1, them)
            else:
                self.create_piece(move.end + 8, 1, them)
        # Case castling
        elif move.specialMoveFlag == 2:
            if move.specialMoveFlag == 2:
                # Moving the rook (king already moved)
                if us:
                    if move.castleSide:
                        self.unmove_piece(7, 5, us, 4)
                    else:
                        self.unmove_piece(0, 3, us, 4)
                else:
                    if move.castleSide:
                        self.unmove_piece(63, 61, us, 4)
                    else:
                        self.unmove_piece(56, 59, us, 4)
        # Case promotion
        elif move.specialMoveFlag == 3:
            self.pieces[CONSTANTS.COLORED_PIECES[us][move.promotionPieceType - 1]] ^= 0b1 << move.end


# Display bitboard in a more readable way
def str_bit_board(bits: int) -> str:
    arr = []
    for i in range(8):
        string = '|'
        for j in range(8):
            bit = bits & 0b1
            string += str(bit)
            string += '|'
            bits = bits >> 1
        string += '\n'
        arr.append(string)
    arr.reverse()
    s = ''
    return s.join(arr)


# Returns 64 chars formated bitboard string
def dump_bitstring(bits):
    return f'{bits:064b}'
