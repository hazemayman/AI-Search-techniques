import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

const data = { array : [1,2,3,4,5] };
function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {


    fetch('/SendData' , {
      method : 'POST',
      headers : {
        'Content-Type' : 'application/json',
      },
      body : JSON.stringify(data)
    })
    .then(res => res.json())
    
    .then(data => {
      console.log('success' , data.array);
      setCurrentTime(data.array)
    }).catch((error) => {
      console.error('error : ' , error);
    });


  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;