import React, { Component } from 'react';
import Text from './mapping.jpg';
class Mapping extends Component {
  render() {
    return (
      <div className="Mapping">
          <img src={Text} alt="Logo" id ="title" />
          We want to help you find the nearest location if you
           are in need of help. 
      </div>
    )
  }
}
export default Mapping;
