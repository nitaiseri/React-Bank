import './App.css';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import React, { useState, useEffect } from 'react';
import Home from './components/Home';
import Transatcions from "./components/Transactions";
import Operations from "./components/Operations"
import Breakdown from "./components/Breakdown"
import User from './models/User'
import axios from 'axios'

function App() {
  const [user, setUser] = useState({id: 1});

  const updateUser = async () => {
    axios.get(`http://localhost:8000/user/${user.id}`)
      .then((result) => {
        setUser(new User(result.data))
      })
      .catch()
  }

  useEffect(() => { updateUser() }, [])

  const updateUserBalance = async (amount) => {
      const newBalance = user.balance + amount
        axios.patch(`http://localhost:8000/user/balance/${user.id}`,
            {balance: newBalance} 
        )
        .then(() => {updateUser()});
    }

  return (
    <Router>
      <div className="App">
        <Route path="/" exact component={() => <Home user={user} />} />
        <Route path="/transactions" exact render={() => <Transatcions user={user} updateBalance={updateUserBalance}/>} />
        <Route path="/operations" exact render={() => <Operations user={user} updateBalance={updateUserBalance}/>} />
        <Route path="/breakdown" exact render={() => <Breakdown user={user} />} />
      </div>
    </Router>
  );
}

export default App;
