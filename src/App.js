import React, { Component } from 'react';
import logo from './images/fruits.svg';
import 'typeface-roboto'
import './App.css';
import heroImage from './images/elaine-casap-86020.jpg'
import ButtonAppBar from './ButtonAppBar'

import cyan from 'material-ui/colors/cyan';
import orange from 'material-ui/colors/orange';

const primary = cyan[900]; // #006064
const accent = orange[600]; // #FB8C00

class App extends Component {
  render() {
    return (
      <div className="App hero-image">
        <ButtonAppBar title='Neighborful' />
        <img src={heroImage} className='img-responsive' width='100%'/>
      </div>
    );
  }
}

export default App;
