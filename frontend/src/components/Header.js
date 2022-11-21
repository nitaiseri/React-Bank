import React from 'react';
import { Link } from 'react-router-dom'
import Balance from './Balance';


function Header(props) {
    console.log("header")
    return (
        <div className='header'>
            <span id="main-links">
                <Link to="/transactions"> Transactions</Link>
                <Link to="/operations"> Operations</Link>
                <Link to="/breakdown"> Breakdown</Link>
            </span>
            <Balance balance={props.balance}></Balance>
        </div>
    );
}

export default Header;