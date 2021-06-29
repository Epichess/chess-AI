class Bitboard:
    def __init__(self, fen):
        self.dict = {
            'r': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'n': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'b': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'q': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'k': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'p': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'R': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'N': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'B': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'Q': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'K': 0b0000000000000000000000000000000000000000000000000000000000000000,
            'P': 0b0000000000000000000000000000000000000000000000000000000000000000,
        }
        i = 64
        for p in fen.split(' ')[0]:
            i -= 1 if ord(p) > 57 else ord(p) - 48 if ord(p) > 47 else 0
            if i < 0 or p not in self.dict:
                continue
            self.dict[p] += 2 ** i

    def dump_board(self, p):
        print("Bitstring: " + self.dump_bitstring(self.dict[p]))
        board = list(self.dump_bitstring(self.dict[p]))

        print("\nBitboard: {0}\n".format(p))
        for i in range(0, 8):
            print(' '.join(board[slice(i * 8, i * 8 + 8)]))

    def dump_bitstring(self, bits):
        return f'{bits:064b}'

    def get_fen(self):
        fen = ""
        tmp = 0
        for i in range(0, 64):
            found = False
            if i > 0 and i % 8 == 0:
                if tmp > 0:
                    fen += str(tmp)
                    tmp = 0
                fen += '/'

            for key, value in self.dict.items():
                value = list(f'{value:064b}')
                if value[i] == '1':
                    if tmp > 0:
                        fen += str(tmp)
                        tmp = 0
                    fen += key
                    found = True
                    break
            if not found:
                tmp += 1
        return fen


class Move:
    start: int
    end: int
    flag: int
    promotedPiece: int


def str_bit_board(bits: int) -> str:
    arr = []
    for i in range(8):
        string = '|'
        for j in range(8):
            bit = bits & 0b1
            string += str(bit)
            string += '|'
            bits = bits >> 1
        string += '\n'
        arr.append(string)
    arr.reverse()
    s = ''
    return s.join(arr)

