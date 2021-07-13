import random
import CONSTANTS


def masked_occup_to_rook_moves(mbit: int, sqr: int) -> int:
    # mbit is a masked bit board, sqr is between 0-63 and represents the index of the starting square of the sliding
    # piece
    rank_index = sqr // 8
    file_index = sqr % 8
    avail_moves = 0b0
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (8 * rank_index) != 0:
            break
        shifter >>= 1
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (8 * rank_index + 7) != 0:
            break
        shifter <<= 1
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << file_index != 0:
            break
        shifter >>= 8
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (56 + file_index) != 0:
            break
        shifter <<= 8
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    avail_moves ^= 0b1 << sqr
    return avail_moves


def masked_occup_to_bishop_moves(mbit: int, sqr: int) -> int:
    # mbit is a masked bit board, sqr is between 0-63 and represents the index of the starting square of the sliding
    # piece

    top_rank = 0xFF00000000000000
    bottom_rank = 0xFF
    left_file = 0b0000000100000001000000010000000100000001000000010000000100000001
    right_file = 0b1000000010000000100000001000000010000000100000001000000010000000
    avail_moves = 0b0
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & top_rank != 0 or shifter & left_file != 0:
            break
        shifter <<= 7
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & top_rank != 0 or shifter & right_file != 0:
            break
        shifter <<= 9
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & bottom_rank != 0 or shifter & left_file != 0:
            break
        shifter >>= 9
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & bottom_rank != 0 or shifter & right_file != 0:
            break
        shifter >>= 7
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    avail_moves ^= 0b1 << sqr
    return avail_moves


def gen_perms(n: int, shifter: int, increment: int, current: int, shift: int, result: set[int]):
    if shifter >= 1 << n * increment:
        result.add(current << shift)
    else:
        gen_perms(n, shifter << increment, increment, current, shift, result)
        gen_perms(n, shifter << increment, increment, current | shifter, shift, result)


def gen_rook_blockers(sqr: int) -> set[int]:
    hset = set()
    vset = set()
    blockers = set()
    n = sqr // 8
    m = sqr % 8
    gen_perms(6, 0b1, 1, 0, 8 * n + 1, hset)
    gen_perms(6, 0b1, 8, 0, 8 + m, vset)
    for h in hset:
        for v in vset:
            blockers.add(h | v | 1 << sqr)
    return blockers


def gen_bishop_blockers(sqr: int) -> set[int]:
    neset = set()
    nwset = set()
    blockers = set()
    n = sqr // 8
    m = sqr % 8
    ne_index = n - m
    nw_index = n + m - 7
    ne_size = max(abs(abs(ne_index) - 7) - 1, 0)
    nw_size = max(abs(abs(nw_index) - 7) - 1, 0)
    if nw_index <= 0:
        gen_perms(nw_size, 1, 7, 0, 14 + nw_index, nwset)
    else:
        gen_perms(nw_size, 1, 7, 0, 14 + nw_index * 8, nwset)
    if ne_index <= 0:
        gen_perms(ne_size, 1, 9, 0, 9 - ne_index, neset)
    else:
        gen_perms(ne_size, 1, 9, 0, 9 + ne_index * 8, neset)
    for nwd in nwset:
        for ned in neset:
            blockers.add(nwd | ned | 1 << sqr)
    return blockers


def magic_hash(bitboard: int, magic_number: int, right_shift: int) -> int:
    return ((bitboard * magic_number) & CONSTANTS.FULL) >> right_shift


def gen_magic_number(sqr: int, gen_blockers, gen_attacks, min_r_shift: int = 60, max_try: int = 100000) -> (tuple[int, int], dict[int, int]):
    blockers = gen_blockers(sqr)
    atk_map = dict()
    for b in blockers:
        atk_map[b] = gen_attacks(b, sqr)
    mhash_map = None
    magic_number = 0
    r_shift = 0
    found_magic = False
    found_rshift = False
    counter = 0
    while not found_magic:
        counter += 1
        if counter > max_try:
            min_r_shift -= 1
            counter = 0
        if counter % 100000 == 0:
            print(counter)
        magic_number = random.getrandbits(64) & random.getrandbits(64) & random.getrandbits(64) & random.getrandbits(64)
        r_shift = 54
        while not found_rshift and r_shift >= min_r_shift:
            mhash_map = dict()
            found_rshift = True
            for b in blockers:
                atks = atk_map[b]
                mhash = magic_hash(b, magic_number, r_shift)
                if mhash in mhash_map:
                    if not mhash_map[mhash] == atks:
                        r_shift -= 1
                        found_rshift = False
                        break
                else:
                    mhash_map[mhash] = atks
        if found_rshift:
            found_magic = True
    return (magic_number, r_shift), mhash_map


def gen_magic_hashtable(sqr: int, magic_number: int, r_shift: int, gen_blockers, gen_attacks) -> (bool, dict[int, int]):
    blockers = gen_blockers(sqr)
    result = dict()
    for b in blockers:
        mhash = magic_hash(b, magic_number, r_shift)
        atk = gen_attacks(b, sqr)
        if mhash in result:
            if not result[mhash] == atk:
                return False, None
        else:
            result[mhash] = atk
    return True, result
