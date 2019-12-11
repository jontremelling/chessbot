import React, { useEffect } from 'react';
import { setAlert } from "../actions/alertActions";
import { initialise, movePiece, getPieces } from '../actions/chessActions';
import { connect } from "react-redux";
import PropTypes from "prop-types";
const Chess = require('react-chess')

const Board = ({ chess: { token, pieces }, initialise, movePiece, getPieces, setAlert }) => {
	useEffect(() => {
        if (localStorage.token) {
            getPieces();
        } else {
            initialise(true);
        }

        // eslint-disable-next-line
    }, []);

	function handleMovePiece(piece, fromSquare, toSquare) {
        movePiece(piece, fromSquare, toSquare);
	}

	return (
		<div className="container" id="board">
            { pieces && pieces.length >0 && <Chess pieces={pieces[0]} onMovePiece={handleMovePiece} /> }
            { <span>{token}</span>}
		</div>
	);
};

Board.propTypes = {
    chess: PropTypes.object.isRequired,
    initialise: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
    chess: state.chess
});

export default connect(
    mapStateToProps,
    { initialise, movePiece, getPieces, setAlert }
)(Board);