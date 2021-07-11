import logo from './logo.png';
import './App.css';
import React from 'react';
import Information from './components/information';
import Home from './components/home';
import Mapping from './components/mapping';
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
      <Router>
          <section className="header">
      <section className="header-top">
        <section className="header-top__logo">
          <img src={logo} className="App-logo" alt="logo" />
        </section>
        <section className="header-top__navbar">
          <section className="header-top__navigation">
        <section className = "navbar">
          <p className="navbar-item">
              <NavLink 
                className="navbar-item"
                exact to="/" 
                activeClassName="selected">
                Home
              </NavLink>
          </p>
          <p className="navbar-item">
              <NavLink
                to="./information" 
                activeClassName="selected">
                Information for me
              </NavLink>
        </p>
        <p className="navbar-item">
              <NavLink
                to="./mapping" 
                activeClassName="selected">
                Find a Health Center
              </NavLink>
        </p>
        </section>
          </section>
          <hr className="header-top__seperator" />
        </section>
      </section>
      
      </section>
      <Switch>
          <Route path="/mapping" component = {Mapping}>  
              </Route>
          <Route path="/information" component = {Information}>
            </Route>
          <Route path="/" component = {Home}>  
          </Route>
      </Switch>
      </Router>

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
