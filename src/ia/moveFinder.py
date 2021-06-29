import math


def get_index(bits):
    i = 0
    for b in bits:
        if b == 1:
            return i
        i += 1


def get_row(i):
    return math.floor(i / 8)


def get_col(i):
    return i - (get_row(i) * 8)


def safe_remove(array, indexes):
    for i in indexes:
        try:
            array.remove(i)
        except:
            pass


def get_knight_moves():
    knights = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)

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


def get_king_moves():
    kings = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)

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


def get_black_pawn_capture():
    pawns = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)

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


def get_white_pawn_capture():
    pawns = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)

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


def get_white_pawn_move():
    pawns = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)

        ind = [8, 16]
        if row != 1:
            safe_remove(ind, [16])
        if row == 7:
            safe_remove(ind, [8, 16])

        for n in ind:
            if (n < 0):
                a = a | (b << abs(n))
            else:
                a = a | (b >> n)
        a -= 2 ** (63 - i)
        pawns[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return pawns


def get_black_pawn_move():
    pawns = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)
        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)

        ind = [-8, -16]
        if row != 6:
            safe_remove(ind, [-16])
        if row == 7:
            safe_remove(ind, [-8, -16])

        for n in ind:
            if (n < 0):
                a = a | (b << abs(n))
            else:
                a = a | (b >> n)
        a -= 2 ** (63 - i)
        pawns[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return pawns


def get_magic_line_mask():
    masks = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
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

        masks[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return masks


def get_magic_diagonal_mask():
    masks = {}

    for i in range(0, 64):
        row = get_row(i)
        col = get_col(i)

        a = 0b0000000000000000000000000000000000000000000000000000000000000000
        a += 2 ** (63 - i)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(7 - row):
            # if (get_row(8 * j - j) != row + j):
            #     break
            a |= b >> (8 * j - j)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(row):
            # if (get_row(8 * j + j) != row - j):
            #     break
            a |= b << (8 * j + j)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(7 - col):
            # if (get_col(8 * j + j) != col + j):
            #     break
            a |= b >> (j + 8 * j)

        b = 0b0000000000000000000000000000000000000000000000000000000000000000
        b += 2 ** (63 - i)
        for j in range(col):
            # if (get_col(8 * j + j) != col - j):
            #     break
            a |= b << (j + 8 * j)

        masks[i] = int('0b' + f'{a:064b}'[::-1], 2)
    return masks

#