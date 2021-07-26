from src.ia.search import evaluate
from src.ia.chessBitBoard import Bitboard


def test_evaluate():
    assert evaluate(Bitboard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')) == 0
    assert evaluate(Bitboard('rnbqkbnr/pppppppp/8/8/8/8/P1PPPPPP/RNBQKBNR w KQkq - 0 1')) == -1
    assert evaluate(Bitboard('rnbqkbnr/pppppppp/8/8/8/8/P1PPPPPP/RNB1KBNR w KQkq - 0 1')) == -10
    assert evaluate(Bitboard('rnbqkbnr/pppppppp/8/6RR/6RR/8/P1PPPPPP/RNB1KBNR w KQkq - 0 1')) == 10
    assert evaluate(Bitboard('rnbqkbnr/pppppppp/8/6RR/6RR/8/P1PPPPPP/RNB2BNR w kq - 0 1')) == -990
