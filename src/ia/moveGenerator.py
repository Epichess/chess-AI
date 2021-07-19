from moveTable import gen_knight_moves_table, gen_king_moves_table, gen_black_pawn_capture_table, \
    gen_black_pawn_move_table, gen_white_pawn_capture_table, gen_white_pawn_move_table, get_magic_line_mask, \
    get_magic_diagonal_mask
from magic_moves import gen_bishop_blockers, gen_rook_blockers, masked_occup_to_bishop_moves, \
    masked_occup_to_rook_moves, gen_magic_hashtable
import CONSTANTS
from move import Move
from bit_utils import extract_index
from chessBitBoard import str_bit_board
from magic_moves import magic_hash


class MoveGenerator:
    knight_move_table: dict[int, int]  # dict[sqr, bitb]
    king_move_table: dict[int, int]  # dict[sqr, bitb]
    black_pawns_capture: dict[int, int]  # dict[sqr, bitb]
    black_pawns_moves: dict[int, int]  # dict[sqr, bitb]
    white_pawns_capture: dict[int, int]  # dict[sqr, bitb]
    white_pawns_moves: dict[int, int]  # dict[sqr, bitb]

    magic_line_masks: dict[int, int]  # dict[sqr, bitb]
    magic_diagonal_masks: dict[int, int]  # dict[sqr, bitb]
    bishop_hash_table: dict[int, dict[int, int]]  # dict[sqr, dict[bitb_hash, bitb]]
    rook_hash_table: dict[int, dict[int, int]]  # dict[sqr, dict[bitb_hash, bitb]]
    bishop_magic: dict[int, (int, int)]  # dict[sqr, (magic_number, right_shift)]
    rook_magic: dict[int, (int, int)]  # dict[sqr, (magic_number, right_shift)]

    def __init__(self):
        # Bitboard movement maps
        self.knight_move_table = gen_knight_moves_table()
        self.king_move_table = gen_king_moves_table()
        self.black_pawns_capture = gen_black_pawn_capture_table()
        self.black_pawns_moves = gen_black_pawn_move_table()
        self.white_pawns_capture = gen_white_pawn_capture_table()
        self.white_pawns_moves = gen_white_pawn_move_table()

        self.magic_line_masks = get_magic_line_mask()
        self.magic_diagonal_masks = get_magic_diagonal_mask()
        self.bishop_hash_table = dict()
        self.rook_hash_table = dict()
        self.rook_magic = CONSTANTS.ROOK_MAGIC
        self.bishop_magic = CONSTANTS.BISHOP_MAGIC

        for i in range(64):
            self.bishop_hash_table[i] = gen_magic_hashtable(i, CONSTANTS.BISHOP_MAGIC[i][0],
                                                            CONSTANTS.BISHOP_MAGIC[i][1], gen_bishop_blockers,
                                                            masked_occup_to_bishop_moves)[1]
            self.rook_hash_table[i] = gen_magic_hashtable(i, CONSTANTS.ROOK_MAGIC[i][0],
                                                          CONSTANTS.ROOK_MAGIC[i][1], gen_rook_blockers,
                                                          masked_occup_to_rook_moves)[1]

    @staticmethod
    def gen_sliding_piece_attacks(move_hash_table: dict[int, dict[int, int]], magic: (int, int),
                                  mask_table: dict[int, int], piece_start_sqr: int, occupancy: int) -> int:
        # For the start square, get the corresponding mask and masked occupancy
        masked_occupancy = mask_table[piece_start_sqr] & occupancy
        # Magic hash the masked occupancy and find its result in the hash table to get the attacks
        return move_hash_table[piece_start_sqr][
            magic_hash(masked_occupancy, magic[piece_start_sqr][0], magic[piece_start_sqr][1])]

    @staticmethod
    def gen_non_sliding_piece_attacks(piece_move_table: dict[int, int], piece_start_sqr) -> int:
        return piece_move_table[piece_start_sqr]

    def gen_bishop_attacks(self, start_sqr: int, occupancy: int) -> int:
        return self.gen_sliding_piece_attacks(self.bishop_hash_table, self.bishop_magic, self.magic_diagonal_masks,
                                              start_sqr, occupancy)

    def gen_rook_attacks(self, start_sqr: int, occupancy: int) -> int:
        return self.gen_sliding_piece_attacks(self.rook_hash_table, self.rook_magic, self.magic_line_masks,
                                              start_sqr, occupancy)

    def gen_queen_attacks(self, start_sqr: int, occupancy: int) -> int:
        return self.gen_bishop_attacks(start_sqr, occupancy) | self.gen_rook_attacks(start_sqr, occupancy)

    @staticmethod
    def gen_piece_captures_from_attacks(start_sqr: int, attacks: int, piece_type: int, us_pieces: int, them_pawns: int,
                                        them_knights: int, them_bishop: int,
                                        them_rooks: int, them_queens: int, them_pieces: int, special_move_flag=0,
                                        promotion_piece_type=0) -> list[Move]:
        result = []
        for end_sqr in extract_index(attacks & them_pawns):
            result.append(Move(start_sqr, end_sqr, piece_type, 1, 1, special_move_flag, promotion_piece_type))
        for end_sqr in extract_index(attacks & them_knights):
            result.append(Move(start_sqr, end_sqr, piece_type, 1, 2, special_move_flag, promotion_piece_type))
        for end_sqr in extract_index(attacks & them_bishop):
            result.append(Move(start_sqr, end_sqr, piece_type, 1, 3, special_move_flag, promotion_piece_type))
        for end_sqr in extract_index(attacks & them_rooks):
            result.append(Move(start_sqr, end_sqr, piece_type, 1, 4, special_move_flag, promotion_piece_type))
        for end_sqr in extract_index(attacks & them_queens):
            result.append(Move(start_sqr, end_sqr, piece_type, 1, 5, special_move_flag, promotion_piece_type))
        return result

    @staticmethod
    def gen_piece_puremoves_from_attacks(start_sqr: int, attacks: int, piece_type: int, us_pieces: int, them_pawns: int,
                                         them_knights: int, them_bishop: int,
                                         them_rooks: int, them_queens: int, them_pieces: int, special_move_flag=0,
                                         promotion_piece_type=0) -> list[Move]:
        result = []
        for end_sqr in extract_index((attacks & ~us_pieces) & (attacks & ~them_pieces)):
            result.append(Move(start_sqr, end_sqr, piece_type, 0, 0, special_move_flag, promotion_piece_type))
        return result

    def gen_piece_moves_from_attacks(self, start_sqr, attacks, piece_type: int, us_pieces: int, them_pawns: int,
                                     them_knights: int, them_bishop: int,
                                     them_rooks: int, them_queens: int, them_pieces: int, special_move_flag=0,
                                     promotion_piece_type=0) -> list[Move]:
        r1 = self.gen_piece_puremoves_from_attacks(start_sqr, attacks, piece_type, us_pieces, them_pawns, them_knights,
                                                   them_bishop, them_rooks, them_queens, them_pieces, special_move_flag,
                                                   promotion_piece_type)
        r2 = self.gen_piece_captures_from_attacks(start_sqr, attacks, piece_type, us_pieces, them_pawns, them_knights,
                                                  them_bishop, them_rooks, them_queens, them_pieces, special_move_flag,
                                                  promotion_piece_type)
        return r1 + r2

    def gen_pieces_moves(self, piece_move_table: dict[int, int], pieces_position: int, piece_type: int, us_pieces: int,
                         them_pawns: int, them_knights: int, them_bishop: int, them_rooks: int, them_queens: int,
                         them_pieces: int) -> list[Move]:
        result = []
        for start_sqr in extract_index(pieces_position):
            attacks = piece_move_table[start_sqr]
            result += self.gen_piece_moves_from_attacks(start_sqr, attacks, piece_type, us_pieces, them_pawns,
                                                        them_knights, them_bishop, them_rooks, them_queens,
                                                        them_pieces)
        return result

    def gen_pieces_captures(self, piece_capture_table: dict[int, int], pieces_position: int, piece_type: int,
                            us_pieces: int,
                            them_pawns: int, them_knights: int, them_bishop: int, them_rooks: int, them_queens: int,
                            them_pieces: int, special_move_flag=0, promotion_piece_type=0) -> list[Move]:
        result = []
        for start_sqr in extract_index(pieces_position):
            attacks = piece_capture_table[start_sqr]
            result += self.gen_piece_captures_from_attacks(start_sqr, attacks, piece_type, us_pieces, them_pawns,
                                                           them_knights, them_bishop, them_rooks, them_queens,
                                                           them_pieces, special_move_flag, promotion_piece_type)
        return result

    def gen_pieces_puremoves(self, piece_move_table: dict[int, int], pieces_position: int, piece_type: int,
                             us_pieces: int,
                             them_pawns: int, them_knights: int, them_bishop: int, them_rooks: int, them_queens: int,
                             them_pieces: int, special_move_flag=0, promotion_piece_type=0) -> list[Move]:
        result = []
        for start_sqr in extract_index(pieces_position):
            attacks = piece_move_table[start_sqr]
            result += self.gen_piece_puremoves_from_attacks(start_sqr, attacks, piece_type, us_pieces, them_pawns,
                                                            them_knights, them_bishop, them_rooks, them_queens,
                                                            them_pieces, special_move_flag, promotion_piece_type)
        return result

    def gen_knight_moves(self, knight_position: int, us_pieces: int, them_pawns: int,
                         them_knights: int, them_bishop: int, them_rooks: int, them_queens: int, them_pieces: int) -> \
            list[Move]:
        return self.gen_pieces_moves(self.knight_move_table, knight_position, 2, us_pieces, them_pawns,
                                     them_knights, them_bishop, them_rooks, them_queens, them_pieces)

    def gen_king_moves(self, king_position: int, us_pieces: int, them_pawns: int, them_knights: int,
                       them_bishop: int, them_rooks: int, them_queens: int, them_pieces: int) -> list[Move]:
        return self.gen_pieces_moves(self.king_move_table, king_position, 6, us_pieces, them_pawns,
                                     them_knights, them_bishop, them_rooks, them_queens, them_pieces)

    def gen_sliding_piece_moves(self, move_hash_table: dict[int, dict[int, int]], magic: (int, int),
                                mask_table: dict[int, int], piece_position: int,
                                piece_type: int, us_pieces: int, them_pawns: int, them_knights: int, them_bishop: int,
                                them_rooks: int, them_queens: int, them_pieces: int, occupancy: int) -> list[Move]:
        result = []
        # Iterate over all piece square
        for start_sqr in extract_index(piece_position):
            # For each square, get the corresponding attacks
            attacks = self.gen_sliding_piece_attacks(move_hash_table, magic, mask_table, start_sqr, occupancy)
            # Using the attacks, do the process of move generation
            result.extend(self.gen_piece_moves_from_attacks(start_sqr, attacks, piece_type, us_pieces, them_pawns,
                                                            them_knights, them_bishop, them_rooks, them_queens,
                                                            them_pieces))
        return result

    def gen_bishop_move(self, bishop_position, us_pieces: int, them_pawns: int, them_knights: int, them_bishop: int,
                        them_rooks: int, them_queens: int, them_pieces: int, occupancy: int):
        return self.gen_sliding_piece_moves(self.bishop_hash_table, self.bishop_magic, self.magic_diagonal_masks,
                                            bishop_position, 3, us_pieces, them_pawns, them_knights, them_bishop,
                                            them_rooks, them_queens, them_pieces, occupancy)

    def gen_rook_move(self, rook_position, us_pieces: int, them_pawns: int, them_knights: int, them_bishop: int,
                      them_rooks: int, them_queens: int, them_pieces: int, occupancy: int):
        return self.gen_sliding_piece_moves(self.rook_hash_table, self.rook_magic, self.magic_diagonal_masks,
                                            rook_position, 3, us_pieces, them_pawns, them_knights, them_bishop,
                                            them_rooks, them_queens, them_pieces, occupancy)

    def gen_queen_move(self, queen_position, us_pieces: int, them_pawns: int, them_knights: int, them_bishop: int,
                       them_rooks: int, them_queens: int, them_pieces: int, occupancy: int):
        result = []
        for start_sqr in extract_index(queen_position):
            attacks = self.gen_queen_attacks(start_sqr, occupancy)
            result.extend(self.gen_piece_moves_from_attacks(start_sqr, attacks, 5, us_pieces, them_pawns,
                                                            them_knights, them_bishop, them_rooks, them_queens,
                                                            them_pieces))
        return result

    def gen_pawn_moves(self, pawn_position: int, us: bool, us_pieces: int, them_pawns: int, them_knights: int,
                       them_bishop: int, them_rooks: int, them_queens: int, them_pieces: int) -> list[Move]:
        result = []
        pre_promotion_rank_mask = CONSTANTS.MASK_SEVENTH_RANK
        if not us:
            pre_promotion_rank_mask = CONSTANTS.MASK_SECOND_RANK
        pre_promotion_pawns = pre_promotion_rank_mask & pawn_position
        non_preprom_pawns = ~pre_promotion_rank_mask & pawn_position
        capture_table = self.white_pawns_capture if us else self.black_pawns_capture
        move_table = self.white_pawns_moves if us else self.black_pawns_moves
        # Generating pawn captures that do not result in promotion
        result += self.gen_pieces_captures(capture_table, non_preprom_pawns, 1, us_pieces, them_pawns, them_knights,
                                           them_bishop, them_rooks, them_queens, them_pieces)
        # Generating pawn captures and moves that result in promotion
        for i in range(2, 6):
            result += self.gen_pieces_captures(capture_table, pre_promotion_pawns, 1, us_pieces, them_pawns,
                                               them_knights, them_bishop, them_rooks, them_queens, them_pieces, 3, i)
            result += self.gen_pieces_puremoves(move_table, pre_promotion_pawns, 1, us_pieces, them_pawns, them_knights,
                                                them_bishop, them_rooks, them_queens, them_pieces, 3, i)
        return result
