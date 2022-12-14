import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import Header from './Header';


function Home(props) {

    return (
        <div className='home-container'>
            <Header balance={props.user.balance}></Header>
        </div>
    );
}

export default Home;