import React, { useState, useEffect } from 'react';
import Header from './Header';
import Card from 'react-bootstrap/Card';
import '../styles/breakdown.css';
import BreakdownModel from '../models/BreakdownModel'
import axios from 'axios'
import List from '@mui/material/List';


function Breakdown(props) {
    const [breakdown, setBreakdown] = useState([])

    const getBreakdown = async () => {
        axios.get(`http://localhost:8000/transaction/breakdown/${props.user.id}`)
            .then((result) => {
                // console.log(result.data.map(c => new BreakdownModel(c)))
                setBreakdown(result.data.map(c => new BreakdownModel(c)))
            })
            .catch()
    }

    useEffect(() => { getBreakdown() }, [])
    return (
        <div>
            <Header balance={props.user.balance}></Header>
            <div className='breakdown-container'>
                <Card className='breakdown-window' style={{ width: '18rem' }}>
                    <Card.Body>
                        <Card.Text>BREAKDOWN</Card.Text>
                        <List className='transactions-container'>
                            {breakdown.map(b => <Card.Text key={b.category}>{b.category}={b.sum}$</Card.Text>)}
                        </List>

                    </Card.Body>
                </Card>
            </div>
        </div>
    );
}

export default Breakdown;