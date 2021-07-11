import logo from './logo.png';
import './App.css';
import React from 'react';
import Information from './components/information';
import Home from './components/home';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from 'react-router-dom';


function App() {
  return (
    <div className="App">
          <section className="header">
      <section className="header-top">
        <section className="header-top__logo">
          <img src={logo} className="App-logo" alt="logo" />
        </section>
        <section className="header-top__navbar">
          <section className="header-top__navigation">
          <Router>
        <section className = "navbar">
          <a className="navbar-item">
              <NavLink 
                className="navbar-item"
                exact to="/" 
                activeClassName="selected">
                Home
              </NavLink>
          </a>
          <a className="navbar-item">
              <NavLink
                to="/information" 
                activeClassName="selected">
                Information
              </NavLink>
</a>
        </section>
        <Switch>
          <Route path="/information">
            <Information />
          </Route>
          <Route path="/">  
            <Home />
          </Route>
        </Switch>
        </Router>
          </section>
          <hr className="header-top__seperator" />
        </section>
      </section>
      </section>
      <header className="App-header">
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

// import { Header } from './components'

// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <Header />
//     </div>
//   );
// }

// export default App;
