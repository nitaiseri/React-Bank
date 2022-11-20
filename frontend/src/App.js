import './App.css';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import { useState } from 'react';
import Transatcions from "./components/Transactions"
import Home from './components/Home';
import Header from './components/Header';

function App() {
  const [userId, setUserId] = useState(1);
  return (
    <Router>
      <Header userId={userId}></Header>

      <div className="App">
        <Route path="/" exact component={() => <Home userId={userId} />} />
        <Route path="/transactions" exact component={() => <Transatcions userId={userId} />} />
        <Route path="/operations" exact component={() => <Home userId={userId} />} />
        <Route path="/breakdown" exact component={() => <Home userId={userId} />} />
      </div>
    </Router>
  );
}

export default App;
