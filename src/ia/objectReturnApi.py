from move import Move

class ObjectCheckMove:
    target = []

    def __init__(self, target):
        self.target = target

class ObjectMakeMove:
    isMoveValid: bool
    isKingCheck: dict[str, bool]
    isGameOver: bool
    fen: str

    def __init__(self, isMoveValid, isKingCheck, isGameOver, fen):
        self.isMoveValid = isMoveValid
        self.isKingCheck = isKingCheck
        self.isGameOver = isGameOver
        self.fen = fen