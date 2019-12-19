import React, { Fragment } from 'react';
import { Provider } from 'react-redux';
import store from './store';
import Alerts from "./components/layout/Alerts";
import Board from './components/Board';
import Score from './components/layout/Score';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <Provider store={store}>
        <Fragment>
            <div className="container">
                <Alerts />
                <Board></Board>
                <Score></Score>
            </div>
        </Fragment>
    </Provider>
  );
}

export default App;
