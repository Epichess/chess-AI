from chessBitBoard import Bitboard
import CONSTANTS
from bit_utils import extract_index
from move import Move
from queue import PriorityQueue


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


def search(board: Bitboard, current_depth: int, max_depth: int, alpha: float = -float('inf'), beta: float = float('inf')) -> tuple[float, Move or None]:

    evaluation = evaluate(board)
    if abs(evaluation) > 500:
        return evaluation, None
    if current_depth == max_depth:
        return evaluation, None

    # evals contains tuples of Moves and evaluations
    evals = PriorityQueue()
    for move in board.moveGenerator.gen_moves(board):
        # Making the move and not doing anything if it turned out to be illegal

        if board.board_info.us:
            value = -float('inf')
            if not board.make_move(move):
                continue
            best_child_move = search(board, current_depth + 1, max_depth, alpha, beta)
            value = max(value, best_child_move[0])
            board.unmake_move()
            if value >= beta:
                return value, move
            alpha = max(alpha, value)
            best_child_move = (-best_child_move[0], move)
        else:
            value = float('inf')
            if not board.make_move(move):
                continue
            best_child_move = search(board, current_depth + 1, max_depth, alpha, beta)
            value = max(value, best_child_move[0])
            board.unmake_move()
            if value <= alpha:
                return value, move
            beta = max(beta, value)
            best_child_move = (best_child_move[0], move)
        evals.put(best_child_move)
    best_move = evals.get()
    if board.board_info.us:
        best_move = (-best_move[0], best_move[1])
    return best_move
