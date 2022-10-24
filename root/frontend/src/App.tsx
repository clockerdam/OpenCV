import React from 'react';
import logo from './logo.svg';
import './App.css';
import { cvUpload } from './api/api';

function App() {
  return (
    <button onClick={handleClick}>Upload CV</button>
  );

  function handleClick() {
    cvUpload().then(res => 
      console.log(res)
    )
  }
}

export default App;
