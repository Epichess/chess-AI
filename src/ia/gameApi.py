from chessBitBoard import Bitboard, BitBoardMoveGenerator
from bit_utils import extract_index
from move import Move
from objectReturnApi import ObjectCheckMove, ObjectMakeMove
from search import search

class GameChecker:
    board: Bitboard
    moveGenerator: BitBoardMoveGenerator

    def __init__(self, fen: str):
        self.board = Bitboard(fen)
        self.moveGenerator = BitBoardMoveGenerator()
        self.board.check_mate = {'checkmate': False, 'color': None}

    #def checkMove(self, move: Move):
    #    if move in self.moveGenerator.gen_legal_moves(self.board):
    #        return True
    #    else:
    #        return False

    def checkGameIsOver(self):
        if len(self.moveGenerator.gen_legal_moves(self.board)) == 0:
            self.board.check_mate = {'checkmate': True, 'color': self.board.board_info.us}
            return True
        return False
    
    def kingCheck(self, move):
        white_king = extract_index(self.board.pieces['K'])
        black_king = extract_index(self.board.pieces['k'])
        
    def showMove(self, move: int) -> ObjectCheckMove:

        list_move_return: list[Move] = []
    
        list_move = self.moveGenerator.gen_legal_moves(self.board)

        if len(list_move) == 0:
            self.board.check_mate = {'checkmate': True, 'color': self.board.board_info.us}
        else:
            for i in range(len(list_move)):
                if move == list_move[i].start:
                    list_move_return.append(list_move[i])
        return ObjectCheckMove(list_move_return)

    def askMoveAPI(self, start: int):
        moves = []
        list_move = self.moveGenerator.gen_legal_moves(self.board)

        for m in list_move:
            if m.start == start:
                moves.append(m)
        return moves

    def makeMoveAPI(self, start: int, end: int, promotion: int = 0) -> ObjectMakeMove:

        move: Move = 0

        list_move = self.moveGenerator.gen_legal_moves(self.board)
        
        white_king = extract_index(self.board.pieces['K'])
        black_king = extract_index(self.board.pieces['k'])

        us = self.board.board_info.us

        self.board.king_check = {'w': False, 'b': False}

        if len(list_move) == 0:
            self.board.check_mate = {'checkmate': True, 'color': self.board.board_info.us}
        else:
            for i in range(len(list_move)):
                if start == list_move[i].start and end == list_move[i].end:
                    move = list_move[i]
                    if promotion > 0:
                        if list_move[i].promotionPieceType == promotion and list_move[i].specialMoveFlag == 3:
                            move = list_move[i]
                            break
                    else:
                        break
            if move != 0:
                if self.board.make_move(move):
                    is_king_check = self.moveGenerator.gen_attacks(self.board, us)
                    for i in range(len(extract_index(is_king_check))):
                        if us:
                            if black_king[0] == extract_index(is_king_check)[i]:
                                self.board.king_check['b'] = True
                        else:
                            if white_king[0] == extract_index(is_king_check)[i]:
                                self.board.king_check['w'] = True
                    return ObjectMakeMove(True, self.board.king_check, self.board.check_mate, self.board.get_fen())
        return ObjectMakeMove(False, self.board.king_check, self.board.check_mate, self.board.get_fen())

    def makeMoveAI(self) -> ObjectMakeMove:
        move = search(self.board, 0, 1)
        us = self.board.board_info.us
        white_king = extract_index(self.board.pieces['K'])
        black_king = extract_index(self.board.pieces['k'])
        self.board.king_check = {'w': False, 'b': False}
        if move[1] != None:
            if self.board.make_move(move[1]):
                is_king_check = self.moveGenerator.gen_attacks(self.board, us)
                for i in range(len(extract_index(is_king_check))):
                    if us:
                        if black_king[0] == extract_index(is_king_check)[i]:
                            self.board.king_check['b'] = True
                    else:
                        if white_king[0] == extract_index(is_king_check)[i]:
                            self.board.king_check['w'] = True
                return ObjectMakeMove(True, self.board.king_check, self.board.check_mate, self.board.get_fen())
        else:
            return ObjectMakeMove(False, True, True, self.board.get_fen())
        return ObjectMakeMove(False, self.board.king_check, self.board.check_mate, self.board.get_fen())