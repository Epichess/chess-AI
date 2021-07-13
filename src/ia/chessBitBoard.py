from MoveInfo import MoveInfo
from src.ia.bit_utils import extract_index


class Move:
    start: int
    end: int
    flag: int
    promotedPiece: int


# IMPORTANT NOTE : Although we're using ints everywhere, there are different kind of them : int representing squares
# are 0 to 63. int representing bitboards are 0 to 2 ^ 64 - 1, ints representing bitboards hashes vary in size but
# are maximum 2^12 - 1
class Bitboard:
    pieces: dict[str, int]
    occupancy: int
    white_pieces: int
    black_pieces: int

    can_en_passant: bool
    en_passant_sqr: int  # sqr

    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        self.can_en_passant = False
        self.en_passant_square = 0

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
        rev = fen.split(' ')[0].split('/')
        res = []
        for r in rev:
            res.append(r[::-1])
        rev = '/'.join(res)
        for p in rev:
            i -= 1 if ord(p) > 57 else ord(p) - 48 if ord(p) > 47 else 0
            if i < 0 or p not in self.pieces:
                continue
            self.pieces[p] += 2 ** i

        self.white_pieces = self.get_white_pieces()
        self.black_pieces = self.get_black_pieces()
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
        tmp = 0
        for i in range(0, 64):
            found = False
            if i > 0 and i % 8 == 0:
                if tmp > 0:
                    fen += str(tmp)
                    tmp = 0
                fen += '/'

            for key, value in self.pieces.items():
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
        return self.white_pieces | self.black_pieces

    # Generate possible capture map. Inputs : a move_map (bitboard)
    def get_capture_map(self, move_map: int, side: bool):
        enemies = 'rnbqkp' if side else 'RNBQKP'

        captures = 0
        for e in list(enemies):
            c = move_map & self.pieces[e]
            captures |= c
        return captures

    # Get piece type from bitboard index
    def get_piece_by_index(self, index):
        for key, value in self.pieces.items():
            if value & (2 ** index) > 0:
                return key
        return 'None'

    # Generate possible captures MoveInfo list
    def get_captures(self, square, move_map, side, piece):
        captures = self.get_capture_map(move_map, side)

        squares = extract_index(captures)
        cap = []
        if (piece == 'P' and 56 > square > 47) or (piece == 'p' and 7 < square < 16):
            for new_square in squares:
                for l in ['N', 'R', 'B', 'Q']:
                    cap.append(
                        MoveInfo((square, new_square), MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece,
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
        captures = self.get_capture_map(move_map, side)

        moves = 0
        for e in list(allies):
            m = move_map & self.pieces[e]
            moves |= m

        squares = extract_index(move_map ^ moves ^ captures)
        moves = []
        if (piece == 'P' and 56 > square > 47) or (piece == 'p' and 7 < square < 16):
            for new_square in squares:
                for l in ['N', 'R', 'B', 'Q']:
                    moves.append(MoveInfo(
                        (square, new_square), MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece,
                        promotion_piece=l))
        else:
            for new_square in squares:
                moves.append(MoveInfo((square, new_square),
                                      MoveInfo.Side.WHITE if side else MoveInfo.Side.BLACK, piece))
        return moves


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
