import React, { Component } from 'react';
import About from './about.jpg';
import Group from './group.jpg';
class Home extends Component {
  render() {
    return (
      <div className="Home">
          <img src={About} alt="Logo" id ="title"/>
          <p>This application helps young girls learn about menstral health. We want girls to learn about these topics in a colorful and relevent way. </p>
          <p>Our team of Carolina Cassedy, Avanti Shah, Samia Zaman, and Suomo Ammah worked during Hack DTech to create this project. Many of us felt the 
              resources were not available to young girls in an easy to understand way. Therefore, we created proHealthLink. We built this website to link women to health resources and information,
               and most of all to nearby health clinics based on their age.</p>
        
               <img src={Group} alt="Logo"  id ="other"/>
        <h1>Mission Statement</h1>
        <p> This platform aims to be a space for growing girls to learn about and find resources on further exploring questions on their bodies and reproductive capabilities. It aims to do away with judgements and criticisms from others and self on a woman knowing her body.
             With that, we say welcome, and let us know if there is a resource we have missed.
        </p>
      </div>

    )
  }
}
export default Home;