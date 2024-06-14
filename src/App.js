import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom' 
import GlobalStyles from './globalStyles'
import { Navbar, Footer } from './components';
import Home from './pages/HomePage/Home';
import ScrollToTop from './components/ScrollToTop';
import { Element } from 'react-scroll';

function App() {
  return (
    
      <Router>
          <GlobalStyles />
          <ScrollToTop />
          <Navbar />
          <Switch>
            <Route path='/' exact component={Home} />
          </Switch>
          <Element name="contact">
          <Footer/>
          </Element>
      </Router>
        
    
  );
}

export default App;
