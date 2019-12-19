import React, { useEffect } from 'react';
import { initialise } from '../../actions/chessActions';
import { connect } from "react-redux";
import PropTypes from "prop-types";

const Score = ({ chess: { pieces, availableMoves, isCheckmate, isStalemate, winner, board }, initialise}) => {
	useEffect(() => {
        if(isCheckmate) {
            console.log("checkmate = " + isCheckmate);
        }
        // eslint-disable-next-line
    }, [isCheckmate]);

    function resetBoard() {
        initialise();
    }

	return (
		<div className="container">
            <p> Checkmate = {isCheckmate ? "True" : "False"}</p>
            <p> Stalemate = {isStalemate ? "True" : "False"}</p>
            <p>Available Moves: {availableMoves}</p>
            <button onClick={resetBoard}>Reset</button>
		</div>
	);
};

Score.propTypes = {
    chess: PropTypes.object.isRequired,
    initialise: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
    chess: state.chess
});

export default connect(
    mapStateToProps,
    { initialise }
)(Score);