import React from 'react';
import Button from './Button';
import { Link } from 'react-router-dom'
import PersonalInfo from './PersonalInfo';

function Header(props) {
    return (
        <div className='header'>
            <div id="main-links">
                <Link to="/transactions"> Transactions</Link>
                <Link to="/operations"> Operations</Link>
                <Link to="/breakdown"> Breakdown</Link>
            </div>
            <PersonalInfo userId={props.userId}></PersonalInfo>
        </div>
    );
}

export default Header;