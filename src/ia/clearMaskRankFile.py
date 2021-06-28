MASK_RANK: dict[int, int] = dict()
CLEAR_RANK: dict[int, int] = dict()
MASK_FILE: dict[int, int] = dict()
CLEAR_FILE: dict[int, int] = dict()
SQUARE_MASK: dict[int, int] = dict()

# RANK and FILE const definition
RANK_1 = 0
RANK_2 = 1
RANK_3 = 2
RANK_4 = 3
RANK_5 = 4
RANK_6 = 5
RANK_7 = 6
RANK_8 = 7
FILE_1 = 0
FILE_2 = 1
FILE_3 = 2
FILE_4 = 3
FILE_5 = 4
FILE_6 = 5
FILE_7 = 6
FILE_8 = 7

# MASK_RANK, CLEAR_RANK, MASK_FILE, CLEAR_FILE Definitions

MASK_RANK[RANK_8] = 0b11111111
MASK_RANK[RANK_7] = 0b1111111100000000
MASK_RANK[RANK_6] = 0b111111110000000000000000
MASK_RANK[RANK_5] = 0b11111111000000000000000000000000
MASK_RANK[RANK_4] = 0b1111111100000000000000000000000000000000
MASK_RANK[RANK_3] = 0b111111110000000000000000000000000000000000000000
MASK_RANK[RANK_2] = 0b11111111000000000000000000000000000000000000000000000000
MASK_RANK[RANK_1] = 0b1111111100000000000000000000000000000000000000000000000000000000
CLEAR_RANK[RANK_8] = ~MASK_RANK[RANK_8]
CLEAR_RANK[RANK_7] = ~MASK_RANK[RANK_7]
CLEAR_RANK[RANK_6] = ~MASK_RANK[RANK_6]
CLEAR_RANK[RANK_5] = ~MASK_RANK[RANK_5]
CLEAR_RANK[RANK_4] = ~MASK_RANK[RANK_4]
CLEAR_RANK[RANK_3] = ~MASK_RANK[RANK_3]
CLEAR_RANK[RANK_2] = ~MASK_RANK[RANK_2]
CLEAR_RANK[RANK_1] = ~MASK_RANK[RANK_1]
MASK_FILE[FILE_8] = 0b1000000010000000100000001000000010000000100000001000000010000000
MASK_FILE[FILE_7] = 0b0100000001000000010000000100000001000000010000000100000001000000
MASK_FILE[FILE_6] = 0b0010000000100000001000000010000000100000001000000010000000100000
MASK_FILE[FILE_5] = 0b0001000000010000000100000001000000010000000100000001000000010000
MASK_FILE[FILE_4] = 0b0000100000001000000010000000100000001000000010000000100000001000
MASK_FILE[FILE_3] = 0b0000010000000100000001000000010000000100000001000000010000000100
MASK_FILE[FILE_2] = 0b0000001000000010000000100000001000000010000000100000001000000010
MASK_FILE[FILE_1] = 0b0000000100000001000000010000000100000001000000010000000100000001
CLEAR_FILE[FILE_8] = ~MASK_FILE[FILE_8]
CLEAR_FILE[FILE_7] = ~MASK_FILE[FILE_7]
CLEAR_FILE[FILE_6] = ~MASK_FILE[FILE_6]
CLEAR_FILE[FILE_5] = ~MASK_FILE[FILE_5]
CLEAR_FILE[FILE_4] = ~MASK_FILE[FILE_4]
CLEAR_FILE[FILE_3] = ~MASK_FILE[FILE_3]
CLEAR_FILE[FILE_2] = ~MASK_FILE[FILE_2]
CLEAR_FILE[FILE_1] = ~MASK_FILE[FILE_1]

# SQUARE_MASK definition

bits = 0b1
for i in range(64):
    SQUARE_MASK[i] = bits
    bits = bits << 1