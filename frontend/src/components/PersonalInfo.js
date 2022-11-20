import React, { useState, useEffect } from 'react';
import User from '../models/User'
import axios from 'axios'

function PersonalInfo(props) {

    const [user, setUser] = useState({})

    useEffect(() => {
        const getUser = async () => {
            const result = await axios.get(`http://localhost:8000/user/${props.userId}`)
            setUser(new User(result.data))
                console.log("inner")
            }
            getUser();
        }, [])

    console.log("Header")
    return (
        <span>
            Hello {user.name}! Balance: {user.balance}$
        </span>
    );
}

export default PersonalInfo;