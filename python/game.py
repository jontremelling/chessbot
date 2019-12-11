import random
import string
import chess
from returnObjects import *

class Game:
  def __init__(self):
    self.board = chess.Board()
    self.tokenObj = {}
        
  def generateToken(self, createdTime, stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    token = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    self.tokenObj = TokenObject(token, createdTime)
    return token

  def getToken(self):
      return self.tokenObj
    
  def updateBoardWithNewMove(self, token, moveFrom, moveTo):
    chosen_move = moveFrom + moveTo       
    move = chess.Move.from_uci(chosen_move)
    if(move in self.board.legal_moves):
        self.board.push_uci(move.uci())
        
  def getReactChessPieces(self):
    positions = []
    output_positions = []
    for p in ['A', 'B', 'C', 'D','E', 'F', 'G', 'H']:
        i=1
        while(i<=8):
           pi = p + str(i)
           positions.append(pi)
           i += 1
    for o in dir(chess):
        if(o in positions):
            e = getattr(chess, o)
            if str(self.board.piece_at(e)) != 'None':
                output_positions.append(str(self.board.piece_at(e)) + '@' + o.lower())
                
    return ', '.join(map(str, output_positions))

  def getAvailableMoves(self):
    available_moves = []
    for i in list(self.board.legal_moves): 
        available_moves.append(str(i)) 
    return ', '.join(map(str, available_moves))

  def getBoardRepresentation(self):
    return self.board.fen().split()[0]