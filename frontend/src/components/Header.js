import React, { useState, useEffect } from 'react';
import Button from './Button';
import { Link } from 'react-router-dom'
import PersonalInfo from './PersonalInfo';
import User from '../models/User'
import axios from 'axios'

function Header(props) {
    const [user, setUser] = useState({});
    const updateUser = async () => {
        await axios.get(`http://localhost:8000/user/${props.userId}`).then((result) => {
            setUser(new User(result.data))
            console.log("inner")
        })
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
            <PersonalInfo user={user}></PersonalInfo>
        </div>
    );
}

export default Header;