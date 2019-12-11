from flask import jsonify
from returnObjects import *
from game import *
from datetime import datetime
import time

class Board:
    def __init__(self):
        self.games = {}
        
    def get_timestamp(self):
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S")) 

    def tokenStillValid(self, tokenTime):
        tokenTime = datetime.strptime(tokenTime, '%Y-%m-%d %H:%M:%S') 
        timeNow = datetime.now()
        
        difference = timeNow - tokenTime
        seconds = difference.total_seconds()
        return seconds < 3600

    def initialise(self):
        game = Game()
        token = game.generateToken(self.get_timestamp(), 6)
        
        self.games[token] = game

        return jsonify(self.games[token].getToken().toString())

    def getPieces(self, token):
        if(token not in self.games):
            return jsonify(ErrorObject(401, "Unauthorised").toString())
        
        if(not self.tokenStillValid(self.games[token].tokenObj.createdTime)):
            return jsonify(ErrorObject(401, "Unauthorised").toString())
        
        return jsonify({
            "pieces": self.games[token].getReactChessPieces(),
            "available_moves": self.games[token].getAvailableMoves(),
            "board": self.games[token].getBoardRepresentation()
        })

    def getBoardArray(self, token):
        return []

    def updateBoardWithNewMove(self, token, moveFrom, moveTo):
        if(not token or token not in self.games):
            return jsonify(ErrorObject(401, "Unauthorised").toString())
        
        if(self.games[token].updateBoardWithNewMove(token, moveFrom, moveTo)):
            return jsonify(ErrorObject(403, "Invalid Move").toString())

        return jsonify({
            "pieces": self.games[token].getReactChessPieces(),
            "available_moves": self.games[token].getAvailableMoves(),
            "board": self.games[token].getBoardRepresentation()
        })