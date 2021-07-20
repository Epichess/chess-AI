class BoardInfo:
    can_en_passant: bool
    en_passant_sqr: int  # sqr
    can_white_queen_side_castle: bool
    can_black_queen_side_castle: bool
    can_white_king_side_castle: bool
    can_black_king_side_castle: bool
    half_move_clock: int
    us: bool

    def __init__(self, can_en_passant, en_passant_sqr, can_white_queen_side_castle, can_black_queen_side_castle,
                 can_white_king_side_castle, can_black_king_side_castle, half_move_clock, us):
        self.can_en_passant = can_en_passant
        self.en_passant_sqr = en_passant_sqr
        self.can_white_queen_side_castle = can_white_queen_side_castle
        self.can_white_king_side_castle = can_white_king_side_castle
        self.can_black_king_side_castle = can_black_king_side_castle
        self.can_black_queen_side_castle = can_black_queen_side_castle
        self.half_move_clock = half_move_clock
        self.us = us
