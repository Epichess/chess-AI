from chessBitBoard import Bitboard
import CONSTANTS
from bit_utils import extract_index


def evaluate(bitboard: Bitboard) -> int:
    white_score = 0
    black_score = 0
    white_score += len(extract_index(bitboard.pieces['P']))
    white_score += 3 * len(extract_index(bitboard.pieces['N']))
    white_score += 3 * len(extract_index(bitboard.pieces['B']))
    white_score += 5 * len(extract_index(bitboard.pieces['R']))
    white_score += 9 * len(extract_index(bitboard.pieces['Q']))
    white_score += 1000 * len(extract_index(bitboard.pieces['K']))
    black_score += len(extract_index(bitboard.pieces['p']))
    black_score += 3 * len(extract_index(bitboard.pieces['n']))
    black_score += 3 * len(extract_index(bitboard.pieces['b']))
    black_score += 5 * len(extract_index(bitboard.pieces['r']))
    black_score += 9 * len(extract_index(bitboard.pieces['q']))
    black_score += 1000 * len(extract_index(bitboard.pieces['k']))
    return white_score - black_score

