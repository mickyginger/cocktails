import React from 'react';
import { withRouter, Link } from 'react-router-dom';

class Navbar extends React.Component {
  state = {
    menuIsOpen: false
  }

  toggleMenu = () => this.setState({ menuIsOpen: !this.state.menuIsOpen })

  componentDidUpdate = (prevProps) => {
    if(prevProps.location.pathname !== this.props.location.pathname)
      this.setState({ menuIsOpen: false });
  }

  render() {
    return (
      <nav className="navbar is-fixed-top">
        <div className="navbar-brand">
          <Link to="/" className="navbar-item">🍸 Classic Cocktails</Link>

          <div
            className={`navbar-burger${this.state.menuIsOpen ? ' is-active' : ''}`}
            onClick={this.toggleMenu}
          >
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>

        <div className={`navbar-menu${this.state.menuIsOpen ? ' is-active' : ''}`}>
          <div className="navbar-end">
            <Link to="/cocktails" className="navbar-item">Browse cocktails</Link>
          </div>
        </div>
      </nav>
    );
  }
}

export default withRouter(Navbar);
