import React, { useState, useEffect } from 'react';
import User from '../models/User'
import axios from 'axios'

function PersonalInfo(props) {

    const [user, setUser] = useState({})

    useEffect(() => {
        axios.get(`http://localhost:8000/user/${props.userId}`).then((result) => {
            setUser(new User(result.data))
        }, [])
    })

    return (
        <span>
            Hello {user.name}! Balance: {user.balance}$
        </span>
    );
}

export default PersonalInfo;