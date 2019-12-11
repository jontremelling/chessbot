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