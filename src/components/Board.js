import React, { useEffect } from 'react';
import { setAlert } from "../actions/alertActions";
import { initialise, movePiece, getPieces } from '../actions/chessActions';
import { connect } from "react-redux";
import PropTypes from "prop-types";
const Chess = require('react-chess')

const Board = ({ chess: { token, pieces, availableMoves, isCheckmate, isStalemate, winner, board }, movePiece, getPieces, setAlert }) => {
	useEffect(() => {
        if(!isCheckmate) {
                getPieces();
        } else {
            setAlert("Checkmate!");
        }
        // eslint-disable-next-line
    }, [isCheckmate]);

	function handleMovePiece(piece, fromSquare, toSquare) {
        let move = fromSquare + toSquare;
        if(availableMoves.includes(move)) {
            movePiece(piece, fromSquare, toSquare);
        } else {
            window.location.reload(false);
        }
	}

	return (
		<div>
            <div className="container" id="board">
                { pieces && pieces.length >0 && <Chess pieces={pieces} onMovePiece={handleMovePiece} /> }
		    </div>
        </div>
	);
};

Board.propTypes = {
    chess: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
    chess: state.chess
});

export default connect(
    mapStateToProps,
    { movePiece, getPieces, setAlert }
)(Board);