
from magic_moves import gen_bishop_blockers, gen_rook_blockers, gen_magic_number, masked_occup_to_bishop_moves, \
    masked_occup_to_rook_moves, gen_magic_hashtable
import CONSTANTS
from moveFinder import get_knight_moves, get_king_moves, get_black_pawn_capture, get_black_pawn_move, get_white_pawn_capture, get_white_pawn_move, get_magic_line_mask, get_magic_diagonal_mask
from MoveInfo import MoveInfo



class Bitboard:
    knights = dict[int, int]
    kings = dict[int, int]
    black_pawns_capture = dict[int, int]
    black_pawns_moves = dict[int, int]
    white_pawns_capture = dict[int, int]
    white_pawns_moves = dict[int, int]

    magic_line_masks = dict[int, int]
    magic_diagonal_masks = dict[int, int]
    bishop_hash_table = dict[int, dict[int, int]]
    rook_hash_table = dict[int, dict[int, int]]

    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        # Bitboard movement maps
        self.knights = get_knight_moves()
        self.kings = get_king_moves()
        self.black_pawns_capture = get_black_pawn_capture()
        self.black_pawns_moves = get_black_pawn_move()
        self.white_pawns_capture = get_white_pawn_capture()
        self.white_pawns_moves = get_white_pawn_move()

        self.magic_line_masks = get_magic_line_mask()
        self.magic_diagonal_masks = get_magic_diagonal_mask()
        self.bishop_hash_table = dict()
        self.rook_hash_table = dict()

        for i in range(64):
            self.bishop_hash_table[i] = gen_magic_hashtable(0, CONSTANTS.BISHOP_MAGIC[0][0],
                                                            CONSTANTS.BISHOP_MAGIC[0][1], gen_bishop_blockers,
                                                            masked_occup_to_bishop_moves)[1]
            self.rook_hash_table[i] = gen_magic_hashtable(0, CONSTANTS.ROOK_MAGIC[0][0],
                                                          CONSTANTS.ROOK_MAGIC[0][1], gen_rook_blockers,
                                                          masked_occup_to_rook_moves)[1]

        self.en_passant = -1

        # Pieces bitboard dictionnary
        self.dict = {
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
        rev = fen.split(' ')[0].split('/')
        res = []
        for r in rev:
            res.append(r[::-1])
        rev = '/'.join(res)
        for p in rev:
            i -= 1 if ord(p) > 57 else ord(p) - 48 if ord(p) > 47 else 0
            if i < 0 or p not in self.dict:
                continue
            self.dict[p] += 2 ** i

    # Retrieve FEN line from dictionnary
    def get_fen(self):
        fen = ""
        tmp = 0
        for i in range(0, 64):
            found = False
            if i > 0 and i % 8 == 0:
                if tmp > 0:
                    fen += str(tmp)
                    tmp = 0
                fen += '/'

            for key, value in self.dict.items():
                value = list(f'{value:064b}')
                if value[i] == '1':
                    if tmp > 0:
                        fen += str(tmp)
                        tmp = 0
                    fen += key
                    found = True
                    break
            if not found:
                tmp += 1
        return fen


    # Generate possible capture map
    def get_capture_map(self, square, move_map, side):
        enemies = 'rnbqkp' if side else 'RNBQKP'

        captures = 0
        for e in list(enemies):
            c = move_map & self.dict[e]
            captures |= c
        if self.en_passant > -1 and ((side and square > 31 and square < 40) or (not side and square > 23 and square < 32)):
            c = move_map & (
                0b0000000000000000000000000000000000000000000000000000000000000000 + (2 ** self.en_passant))
            captures |= c
        return captures

    # Get piece type from bitboard index
    def get_piece_by_index(self, index):
        for key, value in self.dict.items():
            if value & (2 ** index) > 0:
                return key
        return 'None'

    # Generate possible captures MoveInfo list
    def get_captures(self, square, move_map, side, piece):
        captures = self.get_capture_map(square, move_map, side)

        squares = self.extract_index(captures)
        cap = []
        if (piece == 'P' and square < 56 and square > 47) or (piece == 'p' and square > 7 and square < 16):
            for new_square in squares:
                for l in ['N', 'R', 'B', 'Q']:
                    cap.append(MoveInfo((square, new_square), MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece,
                                        captured_piece=self.get_piece_by_index(new_square), promotion_piece=l))
        # elif self.en_passant > -1 and ((piece == 'P' and square < 40 and square > 31) or (piece == 'p' and square > 24 and square < 32)):
        #     b = 2 ** self.en_passant
        #     r =
        else:
            for new_square in squares:
                cap.append(MoveInfo((square, new_square), MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece,
                                    captured_piece=self.get_piece_by_index(new_square)))
        return cap

    # Generate possible moves MoveInfo list
    def get_moves(self, square, move_map, side, piece):
        allies = 'rnbqkp' if not side else 'RNBQKP'
        captures = self.get_capture_map(square, move_map, side)

        moves = 0
        for e in list(allies):
            m = move_map & self.dict[e]
            moves |= m

        squares = self.extract_index(move_map ^ moves ^ captures)
        moves = []
        if (piece == 'P' and square < 56 and square > 47) or (piece == 'p' and square > 7 and square < 16):
            for new_square in squares:
                for l in ['N', 'R', 'B', 'Q']:
                    moves.append(MoveInfo(
                        (square, new_square), MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece, promotion_piece=l))
        else:
            for new_square in squares:
                moves.append(MoveInfo((square, new_square),
                             MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece))
        return moves

    def extract_index(self, bitboard):
        a = []
        for i in range(0, 63):
            if (bitboard & 1 << i != 0):
                a.append(i)
        return a


class Move:
    start: int
    end: int
    flag: int
    promotedPiece: int


# Display all formated moves
def dump_moves(moves):
    for key, value in moves.items():
        print(str_bit_board(value))


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
