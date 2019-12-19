from flask import Flask, render_template, request
from flask_cors import CORS
import connexion
from board import *

# Create the application instance
app = Flask(__name__)
CORS(app)

board = Board()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/api/initialise')
def initialise():
    return board.initialise()

@app.route('/api/pieces')
def getPieces():
    token = request.headers.get('x-auth-token')
    return board.getPieces(token)

@app.route('/api/sendnewmove', methods = ['POST'])
def updateBoardWithNewMove():
    token = request.headers.get('token')
    data = request.get_json()
    moveTo = data["moveTo"]
    moveFrom = data["moveFrom"]
    return board.updateBoardWithNewMove(token, moveFrom, moveTo)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)