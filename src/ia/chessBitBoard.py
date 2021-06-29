from moveFinder import get_knight_moves, get_king_moves, get_black_pawn_capture, get_black_pawn_move, get_white_pawn_capture, get_white_pawn_move, get_magic_line_mask, get_magic_diagonal_mask


class Bitboard:
    knights = dict[int, int]
    kings = dict[int, int]
    black_pawns_capture = dict[int, int]
    black_pawns_moves = dict[int, int]
    white_pawns_capture = dict[int, int]
    white_pawns_moves = dict[int, int]

    magic_line_masks = dict[int, int]
    magic_diagonal_masks = dict[int, int]

    def __init__(self, fen):
        # Bitboard movement maps
        self.knights = get_knight_moves()
        self.kings = get_king_moves()
        self.black_pawns_capture = get_black_pawn_capture()
        self.black_pawns_moves = get_black_pawn_move()
        self.white_pawns_capture = get_white_pawn_capture()
        self.white_pawns_moves = get_white_pawn_move()

        self.magic_line_masks = get_magic_line_mask()
        self.magic_diagonal_masks = get_magic_diagonal_mask()

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
        for p in fen.split(' ')[0]:
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

    # Retrieve possible captures map
    def get_captures(self, piece, index):
        p = piece.lower()
        move_map = (self.knights if p == 'n'
                    else self.kings if p == 'k'
                    else self.black_pawns_capture if piece == 'p'
                    else self.white_pawns_capture)[index]

        captures = (move_map & self.dict['r']) | (
            move_map & self.dict['n']) | (move_map & self.dict['b']) | (
            move_map & self.dict['q']) | (move_map & self.dict['k']) | (
            move_map & self.dict['p'])
        return captures


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
    string = ''
    for i in range(8):
        string += '|'
        for j in range(8):
            bit = bits & 0b1
            string += str(bit)
            string += '|'
            bits = bits >> 1
        string += '\n'
    return string


# Returns 64 chars formated bitboard string
def dump_bitstring(bits):
    return f'{bits:064b}'
