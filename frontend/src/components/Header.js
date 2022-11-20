import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'
import Balance from './Balance';
import User from '../models/User'
import axios from 'axios'

function Header(props) {
    const [user, setUser] = useState({});

    const updateUser = async () => {
        await axios.get(`http://localhost:8000/user/${props.userId}`)
        .then((result) => {
            setUser(new User(result.data))
            console.log("inner")
        })
        .catch()
    }

    useEffect(() => { updateUser() }, [])

    console.log("header")
    return (
        <div className='header'>
            <div id="main-links">
                <Link to="/transactions"> Transactions</Link>
                <Link to="/operations"> Operations</Link>
                <Link to="/breakdown"> Breakdown</Link>
            </div>
            <Balance balance={user.balance}></Balance>
        </div>
    );
}

export default Header;