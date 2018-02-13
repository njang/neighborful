import React, { Component } from 'react';
import logo from './images/fruits.svg';
import 'typeface-roboto'
import './App.css';
import heroImage from './images/caroline-attwood-225496.jpg'

class App extends Component {
  render() {
    return (
      <div className="App hero-image">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Neighborful</h1>
        </header>
        <img src={heroImage} className='img-responsive' width='100%'/>
      </div>
    );
  }
}

export default App;
