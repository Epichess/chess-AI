import src.ia.chessBitBoard as bb
import src.ia.magic_moves as mm

def test_bitboard():
    board = bb.Bitboard('1r6/8/6r1/6r1/6r1/5r2/8/8 w - - 0 1')
    assert(board.pieces['r'] == 0b0000001000000000010000000100000001000000001000000000000000000000)

def test_initial_move_generation():
    board = bb.Bitboard('2q3p1/2bBbb2/8/2b3pb/5b2/1b1R2n1/2b2b2/4b3 w - - 0 1')
    assert(board.occupancy == 0b100010000111100000000001100010000100000010010100010010000010000)
    assert(mm.masked_occup_to_rook_moves(board.occupancy, 19) == 0b1000000010000000100000001000011101100000100000001000)
