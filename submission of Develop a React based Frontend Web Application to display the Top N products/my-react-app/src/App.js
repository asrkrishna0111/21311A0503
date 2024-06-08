import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AllProducts from './AllProducts';
import ProductDetails from './ProductDetails';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={AllProducts} />
        <Route path="/product/:productId" component={ProductDetails} />
      </Switch>
    </Router>
  );
}

export default App;
