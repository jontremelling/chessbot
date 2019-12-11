import { SET_PIECES, INITIALISE_GAME } from "../actions/types";

const initialState = {
    pieces: []
};

export default (state = initialState, action) => {
    switch (action.type) {
        case SET_PIECES:
            return {
                ...state, 
                pieces: [action.payload]
            };
        default:
            return state;
    }
};
