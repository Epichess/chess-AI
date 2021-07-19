def get_row(i) -> int:
    return i // 8


def get_col(i) -> int:
    return i % 8


def safe_remove(array, indexes):
    for i in indexes:
        try:
            array.remove(i)
        except:
            pass


# This function returns an initialized knight move table
def gen_knight_moves_table() -> dict[int, int]:
    knights = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 1 << (63 - i)
        b = 1 << (63 - i)

        ind = [6, -6, 10, -10, 15, -15, 17, -17]
        if col == 0:
            safe_remove(ind, [-10, -17, 6, 15])
        elif col == 1:
            safe_remove(ind, [-10, 6])
        elif col == 6:
            safe_remove(ind, [10, -6])
        elif col == 7:
            safe_remove(ind, [10, 17, -6, -15])

        if row == 0:
            safe_remove(ind, [-10, -17, -6, -15])
        elif row == 1:
            safe_remove(ind, [-17, -15])
        elif row == 6:
            safe_remove(ind, [17, 15])
        elif row == 7:
            safe_remove(ind, [10, 17, 6, 15])

        for n in ind:
            if (n < 0):
                a = a | (b << abs(n))
            else:
                a = a | (b >> n)
        a -= 2 ** (63 - i)
        knights[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return knights


# This function returns an initialized king move table
def gen_king_moves_table():
    kings = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 1 << (63 - i)
        b = 1 << (63 - i)

        ind = [1, -1, 7, -7, 8, -8, 9, -9]
        if col == 0:
            safe_remove(ind, [-1, -9, 7])
        elif col == 7:
            safe_remove(ind, [1, 9, -7])
        if row == 0:
            safe_remove(ind, [-8, -9, -7])
        elif row == 7:
            safe_remove(ind, [8, 9, 7])

        for n in ind:
            if (n < 0):
                a = a | (b << abs(n))
            else:
                a = a | (b >> n)
        a -= 2 ** (63 - i)
        kings[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return kings


# This function returns an initialized black pawn capture table
def gen_black_pawn_capture_table():
    pawns = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 1 << (63 - i)
        b = 1 << (63 - i)

        ind = [-7, -9]
        if col == 0:
            safe_remove(ind, [-9])
        elif col == 7:
            safe_remove(ind, [-7])
        if row == 0:
            safe_remove(ind, [-7, -9])

        for n in ind:
            if (n < 0):
                a = a | (b << abs(n))
            else:
                a = a | (b >> n)
        a -= 2 ** (63 - i)
        pawns[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return pawns


# This function returns an initialized white pawn capture table
def gen_white_pawn_capture_table():
    pawns = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 1 << (63 - i)
        b = 1 << (63 - i)

        ind = [7, 9]
        if col == 0:
            safe_remove(ind, [7])
        elif col == 7:
            safe_remove(ind, [9])
        if row == 0:
            safe_remove(ind, [7, 9])

        for n in ind:
            if (n < 0):
                a = a | (b << abs(n))
            else:
                a = a | (b >> n)
        a -= 2 ** (63 - i)
        pawns[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return pawns


# This function returns an initialized white pawn move table
def gen_white_pawn_move_table() -> dict[int, int]:
    pawns = dict()

    for i in range(0, 64):
        row = get_row(i)

        if row == 7:
            pawns[i] = 0
            continue

        pawns[i] = 1 << i + 8

    return pawns


# This function returns an initialized black pawn move table, that does NOT include the first move 2 squares possibility
def gen_black_pawn_move_table() -> dict[int, int]:
    pawns = dict()

    for i in range(0, 64):
        row = get_row(i)

        if row == 0:
            pawns[i] = 0
            continue

        pawns[i] = 1 << i - 8

    return pawns


def get_magic_line_mask() -> dict[int, int]:
    masks = dict()

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 1 << (63 - i)
        b = 1 << (63 - i)

        for j in range(7 - row):
            a |= b >> (8 * j)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(row):
            a |= b << (8 * j)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(7 - col):
            a |= b >> (j)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(col):
            a |= b << (j)

        # a &= ~ (1 << (63 - i))

        masks[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return masks


def get_magic_diagonal_mask() -> dict[int, int]:
    masks = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 1 << i
        b = 1 << i

        for j in range(1, 7 - row):
            offset = (8 * j + j)
            if get_row(i + offset) == row + j and get_col(i + offset) != 7:
                a |= b << offset

        # Bottom Left
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (i)
        for j in range(1, row):
            offset = (8 * j + j)
            if get_row(i - offset) == row - j and get_col(i - offset) != 0:
                a |= b >> offset

        # Bottom Right
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (i)
        for j in range(1, row):
            offset = (8 * j - j)
            if get_row(i - offset) == row - j and get_col(i - offset) != 7:
                a |= b >> offset

        # Top Left
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (i)
        for j in range(1, 7 - row):
            offset = (8 * j - j)
            if get_row(i + offset) == get_row(i) + j and get_col(i + offset) != 0:
                a |= b << offset
        # a &= ~ (1 << i)

        masks[i] = a
    return masks
