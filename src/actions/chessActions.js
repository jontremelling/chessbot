import axios from 'axios';
import setAuthToken from '../utils/setAuthToken';
import { SET_PIECES, INITIALISE_GAME } from "./types";

// Initialise game
export const initialise = () => async dispatch => {
    try {
        const config = {
            headers: {
                "Content-Type": "application/json",
            }
        };

        axios.get("http://localhost:5000/api/initialise", config)
        .then((res) => {
            const data = res.data;

            localStorage.setItem('token', data.token);
            if (localStorage.token) {
                setAuthToken(localStorage.token);
            } else {
                setAuthToken(data.token);
                localStorage.setItem('token', data.token);
            }

            return axios.get("http://localhost:5000/api/pieces", config);
        })
        .then((res) => {
            const data = res.data;
    
            dispatch({
                type: SET_PIECES,
                payload: data
            })
        })
        .catch((err) => {
            console.log(err.response)
        });
    } catch (err) {
    }
};

export const getPieces = () => async dispatch => {
    try {
        if (localStorage.token) {
            setAuthToken(localStorage.token);

            axios.get("http://localhost:5000/api/pieces")
            .then((res) => {
                const data = res.data;

                if(data.code === 401) {
                    const config = {
                        headers: {
                            "Content-Type": "application/json",
                        }
                    };
                    axios.get("http://localhost:5000/api/initialise", config)
                    .then((res) => {
                        const data = res.data;

                        localStorage.setItem('token', data.token);
                        if (localStorage.token) {
                            setAuthToken(localStorage.token);
                        } else {
                            setAuthToken(data.token);
                            localStorage.setItem('token', data.token);
                        }

                        return axios.get("http://localhost:5000/api/pieces", config);
                    })
                    .then((res) => {
                        const data = res.data;
                
                        dispatch({
                            type: SET_PIECES,
                            payload: data
                        })
                    })
                } else {
                    dispatch({
                        type: SET_PIECES,
                        payload: data
                    })
                }
        
                
            })
            .catch((err) => {
                console.log(err.response)
            });
        }
    } catch (err) {
    }
};

export const movePiece = (piece, from, to) => async dispatch => {
    try {
        if (localStorage.token) {
            setAuthToken(localStorage.token);

            const body = {
                'moveFrom': from,
                'moveTo': to
            }

            const config = {
                headers: {
                    "Content-Type": "application/json",
                    "token": localStorage.token
                }
            };

            const res = await axios.post("http://localhost:5000/api/sendnewmove", body, config);
            const data = res.data;

            dispatch({
                type: SET_PIECES,
                payload: data
            });
        }
    } catch (err) {
        console.log(err);
    }
};
