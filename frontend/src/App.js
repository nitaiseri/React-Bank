import './App.css';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import { useState } from 'react';
import Home from './components/Home';
import Transatcions from "./components/Transactions";
import Operations from "./components/Operations"
import Breakdown from "./components/Breakdown"

function App() {
  const [userId, setUserId] = useState(1);
  return (
    <Router>
      <div className="App">
        <Route path="/" exact component={() => <Home userId={userId} />} />
        <Route path="/transactions" exact render={() => <Transatcions userId={userId} />} />
        <Route path="/operations" exact render={() => <Operations userId={userId} />} />
        <Route path="/breakdown" exact render={() => <Breakdown userId={userId} />} />
      </div>
    </Router>
  );
}

export default App;
