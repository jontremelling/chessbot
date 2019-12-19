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
    else:
        return ErrorObject(400, "Invalid move")
        
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
                
    return output_positions

  def getAvailableMoves(self):
    available_moves = []
    for i in list(self.board.legal_moves): 
        available_moves.append(str(i)) 
    return available_moves

  def getBoardRepresentation(self):
    return self.board.fen().split()[0]

  def determineGameFinished(self):
    return StateObject(
        400 if self.board.is_checkmate() or self.board.is_stalemate() else 200,
        self.board.is_stalemate(), 
        self.board.is_checkmate(), 
        "Draw" if self.board.is_stalemate() else "white" if self.board.turn else "black",
        self.getReactChessPieces(),
        self.getAvailableMoves(),
        self.getBoardRepresentation()
    )
    
  def updateBoardWithRandomMove(self):
    chosen_move = random.choice(self.getAvailableMoves())      
    move = chess.Move.from_uci(chosen_move)
    if(move in self.board.legal_moves):
        self.board.push_uci(move.uci())
        
  def tryToTakeAPiece(self):
    available_positions = {
        "initial": [],
        "end": []
    }

    for i in list(self.board.legal_moves):
        available_positions["initial"].append(str(i)[:2].upper())
        available_positions["end"].append(str(i)[2:].upper()) 
        
            
    for o in dir(chess):
        i = 0
        while i < len(available_positions["end"]):
            if(o == available_positions["end"][i]):
                e = getattr(chess, o)
                print(o)
                if str(self.board.piece_at(e)) != 'None':
                    chosen_move = available_positions["initial"][i] + available_positions["end"][i]
                    for fff in list(self.board.legal_moves): 
                        print(str(fff))
                    print(chosen_move.lower())     
                    move = chess.Move.from_uci(chosen_move.lower())
                    if(move in self.board.legal_moves):
                        self.board.push_uci(move.uci())
                        return 'moved'
            i += 1
            