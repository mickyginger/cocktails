import React from 'react';
import axios from 'axios';

class CocktailsIndex extends React.Component {

  state = {}

  componentDidMount() {
    axios.get('/api/cocktails')
      .then(res => this.setState({ cocktails: res.data }));
  }


  render() {
    if(!this.state.cocktails) return null;
    return (
      <main className="section">
        <div className="container">
          <ul className="columns">
            {this.state.cocktails.map(cocktail =>
              <li key={cocktail.id} className="column is-one-third-desktop is-half-tablet">
                <div className="card">
                  <header className="card-header">
                    <p className="card-header-title">{cocktail.name}</p>
                  </header>

                  <div className="card-image">
                    <figure className="image">
                      <img src={cocktail.image} alt={cocktail.name} />
                    </figure>
                  </div>
                </div>
              </li>
            )}
          </ul>
        </div>
      </main>
    );
  }
}

export default CocktailsIndex;
