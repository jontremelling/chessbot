import { combineReducers } from 'redux';
import alertReducer from './alertReducer';
import chessReducer from './chessReducer';

export default combineReducers({
    alert: alertReducer,
    chess: chessReducer
});
