import React from 'react';
import ReactDOM from 'react-dom';

import { BrowserRouter, Switch, Route } from 'react-router-dom';

import CocktailsIndex from './components/cocktails/CocktailsIndex';
import Navbar from './components/common/Navbar';

import 'bulma';
import './scss/style.scss';

class App extends React.Component {

  render() {
    return (
      <BrowserRouter>
        <div>
          <Navbar />
          <Switch>
            <Route to="/cocktails" component={CocktailsIndex} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
