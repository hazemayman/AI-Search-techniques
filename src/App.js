import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import Board from './Components/Board/Board'
const data = { array : [1,2,3,4,5] };
function App() {
  return (
    <>
    <Board />
    </>
  );
}

export default App;