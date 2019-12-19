class InitialisedObject:  
    def __init__(self, token, pieces):
        self.token = token
        self.pieces = pieces
        
    def toString(self):
      return {
        "token": self.token,
        "pieces": self.pieces   
      }

class SuccessObject:  
    def __init__(self, pieces, takenPieces, board, history, messages, errors):
        self.pieces = pieces
        self.takenPieces = takenPieces
        self.board = board
        self.history = history
        self.messages = messages
        self.errors = errors
        
    def toString(self):
      return {
        "pieces": self.pieces,
        "takenPieces": self.takenPieces,
        "board": self.board,
        "history": self.history,
        "messages": self.messages,
        "errors": self.errors
      }
      
class ErrorObject:  
    def __init__(self, errorCode, errorMessage):
        self.errorCode = errorCode
        self.errorMessage = errorMessage
        
    def toString(self):
      return {
        "code": self.errorCode,
        "message": self.errorMessage 
      }
      
class TokenObject:
    def __init__(self, token, createdTime):
        self.token = token
        self.createdTime = createdTime
        
    def toString(self):
      return {
        "token": self.token,
        "createdTime": self.createdTime 
      }
      
class StateObject:
    def __init__(self, code, is_stalemate, is_checkmate, winner, react_chess_pieces, available_moves, board_representation):
        self.code = code
        self.is_stalemate = is_stalemate
        self.is_checkmate = is_checkmate
        self.winner = winner
        self.pieces = react_chess_pieces
        self.available_moves = available_moves
        self.board_representation = board_representation
        
    def toString(self):
        return {
            "code": self.code,
            "isStalemate": self.is_stalemate,
            "isCheckmate": self.is_checkmate,
            "winner": self.winner,
            "pieces": self.pieces,
            "available_moves": self.available_moves,
            "board": self.board_representation
        }