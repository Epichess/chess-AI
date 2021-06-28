import math


class MoveFinder():
    def __init__(self):
        knights = self.get_knight_moves()
        kings = self.get_king_moves()
        black_pawns_capture = self.get_black_pawn_capture()
        black_pawns_moves = self.get_black_pawn_move()
        white_pawns_capture = self.get_white_pawn_capture()
        white_pawns_moves = self.get_white_pawn_move()

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
        print(f'{bits:064b}')

    def dump_moves(self, moves):
        for key, value in moves.items():
            print(self.str_bit_board(value))

    def safe_remove(self, array, indexes):
        for i in indexes:
            try:
                array.remove(i)
            except:
                pass

    def str_bit_board(self, bits: int) -> str:
        string = ''
        for i in range(8):
            string += '|'
            for j in range(8):
                bit = bits & 0b1
                string += str(bit)
                string += '|'
                bits = bits >> 1
            string += '\n'
        return string

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
                self.safe_remove(ind, [-10, -17, 6, 15])
            elif col == 1:
                self.safe_remove(ind, [-10, 6])
            elif col == 6:
                self.safe_remove(ind, [10, -6])
            elif col == 7:
                self.safe_remove(ind, [10, 17, -6, -15])

            if row == 0:
                self.safe_remove(ind, [-10, -17, -6, -15])
            elif row == 1:
                self.safe_remove(ind, [-17, -15])
            elif row == 6:
                self.safe_remove(ind, [17, 15])
            elif row == 7:
                self.safe_remove(ind, [10, 17, 6, 15])

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            a -= 2 ** (63 - i)
            knights[i] = a
        return knights

    def get_king_moves(self):
        kings = {}

        for i in range(0, 64):
            row = self.get_row(i)
            col = self.get_col(i)

            a = 0b0000000000000000000000000000000000000000000000000000000000000000
            a += 2 ** (63 - i)
            b = 0b0000000000000000000000000000000000000000000000000000000000000000
            b += 2 ** (63 - i)

            ind = [1, -1, 7, -7, 8, -8, 9, -9]
            if col == 0:
                self.safe_remove(ind, [-1, -9, 7])
            elif col == 7:
                self.safe_remove(ind, [1, 9, -7])
            if row == 0:
                self.safe_remove(ind, [-8, -9, -7])
            elif row == 7:
                self.safe_remove(ind, [8, 9, 7])

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            a -= 2 ** (63 - i)
            kings[i] = a
        return kings

    def get_black_pawn_capture(self):
        pawns = {}

        for i in range(0, 64):
            row = self.get_row(i)
            col = self.get_col(i)

            a = 0b0000000000000000000000000000000000000000000000000000000000000000
            a += 2 ** (63 - i)
            b = 0b0000000000000000000000000000000000000000000000000000000000000000
            b += 2 ** (63 - i)

            ind = [-7, -9]
            if col == 0:
                self.safe_remove(ind, [-9])
            elif col == 7:
                self.safe_remove(ind, [-7])
            if row == 0:
                self.safe_remove(ind, [-7, -9])

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            a -= 2 ** (63 - i)
            pawns[i] = a
        return pawns

    def get_white_pawn_capture(self):
        pawns = {}

        for i in range(0, 64):
            row = self.get_row(i)
            col = self.get_col(i)

            a = 0b0000000000000000000000000000000000000000000000000000000000000000
            a += 2 ** (63 - i)
            b = 0b0000000000000000000000000000000000000000000000000000000000000000
            b += 2 ** (63 - i)

            ind = [7, 9]
            if col == 0:
                self.safe_remove(ind, [7])
            elif col == 7:
                self.safe_remove(ind, [9])
            if row == 0:
                self.safe_remove(ind, [7, 9])

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            a -= 2 ** (63 - i)
            pawns[i] = a
        return pawns

    def get_white_pawn_move(self):
        pawns = {}

        for i in range(0, 64):
            row = self.get_row(i)
            col = self.get_col(i)

            a = 0b0000000000000000000000000000000000000000000000000000000000000000
            a += 2 ** (63 - i)
            b = 0b0000000000000000000000000000000000000000000000000000000000000000
            b += 2 ** (63 - i)

            ind = [8, 16]
            if row != 1:
                self.safe_remove(ind, [16])
            if row == 7:
                self.safe_remove(ind, [8, 16])

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            a -= 2 ** (63 - i)
            pawns[i] = a
        return pawns

    def get_black_pawn_move(self):
        pawns = {}

        for i in range(0, 64):
            row = self.get_row(i)
            col = self.get_col(i)

            a = 0b0000000000000000000000000000000000000000000000000000000000000000
            a += 2 ** (63 - i)
            b = 0b0000000000000000000000000000000000000000000000000000000000000000
            b += 2 ** (63 - i)

            ind = [-8, -16]
            if row != 6:
                self.safe_remove(ind, [-16])
            if row == 7:
                self.safe_remove(ind, [-8, -16])

            for n in ind:
                if (n < 0):
                    a = a | (b << abs(n))
                else:
                    a = a | (b >> n)
            a -= 2 ** (63 - i)
            pawns[i] = a
        return pawns
