import math


class MoveFinder():
    def __init__(self):
        knights = self.get_knight_moves()

    def get_index(self, bits):
        i = 0
        for b in bits:
            if b == 1:
                return i
            i += 1

    def get_row(self, i):
        return math.floor(i / 8)

    def get_col(self, i):
        return i - (self.get_row(i) * 8)

    def dump_bitstring(self, bits):
        return f'{bits:064b}'

    def get_knight_moves(self):
        knights = {}

        for i in range(0, 64):
            row = self.get_row(i)
            col = self.get_col(i)

            a = 0b0000000000000000000000000000000000000000000000000000000000000000
            a += 2 ** (63 - i)
            b = 0b0000000000000000000000000000000000000000000000000000000000000000
            b += 2 ** (63 - i)

            ind = [6, -6, 10, -10, 15, -15, 17, -17]
            if col == 0:
                try:
                    ind.remove(-10)
                except:
                    pass
                try:
                    ind.remove(-17)
                except:
                    pass
                try:
                    ind.remove(6)
                except:
                    pass
                try:
                    ind.remove(15)
                except:
                    pass
            elif col == 1:
                try:
                    ind.remove(-10)
                except:
                    pass
                try:
                    ind.remove(6)
                except:
                    pass
            elif col == 6:
                try:
                    ind.remove(10)
                except:
                    pass
                try:
                    ind.remove(-6)
                except:
                    pass
            elif col == 7:
                try:
                    ind.remove(10)
                except:
                    pass
                try:
                    ind.remove(17)
                except:
                    pass
                try:
                    ind.remove(-6)
                except:
                    pass
                try:
                    ind.remove(-15)
                except:
                    pass

            if row == 0:
                try:
                    ind.remove(-10)
                except:
                    pass
                try:
                    ind.remove(-17)
                except:
                    pass
                try:
                    ind.remove(-6)
                except:
                    pass
                try:
                    ind.remove(-15)
                except:
                    pass
            elif row == 1:
                try:
                    ind.remove(-15)
                except:
                    pass
                try:
                    ind.remove(-17)
                except:
                    pass
            elif row == 6:
                try:
                    ind.remove(15)
                except:
                    pass
                try:
                    ind.remove(17)
                except:
                    pass
            elif row == 7:
                try:
                    ind.remove(10)
                except:
                    pass
                try:
                    ind.remove(17)
                except:
                    pass
                try:
                    ind.remove(6)
                except:
                    pass
                try:
                    ind.remove(15)
                except:
                    pass

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            knights[i] = a
        return knights
