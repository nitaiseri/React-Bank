import Transaction from './Transaction';
import React, { useState, useEffect } from 'react';
import Header from './Header';
import TransactionModel from '../models/Transaction'
import axios from 'axios'
import List from '@mui/material/List';
import '../styles/transactions.css'

function Transatcions(props) {
    const [transactions, setTransactions] = useState([])

    const getTransactions = async () => {
        axios.get(`http://localhost:8000/transaction/${props.user.id}`)
            .then((result) => {
                setTransactions(result.data.map(r => new TransactionModel(r)))
                console.log("inner")
            })
            .catch()
    }

    useEffect(() => { getTransactions() }, [])

    const deleteTransaction = async (transactionId) => {
        axios.delete(`http://localhost:8000/transaction/${transactionId}`)
        .then(() => {getTransactions()});
    }

    return (
        <div >
            <Header balance={props.user.balance}></Header>
            <List className='transactions-container'>
                {transactions.map((t, k) => <Transaction key={k} transaction={t} deleteTransaction={deleteTransaction} updateBalance={props.updateBalance}></Transaction>)}
            </List>
        </div>
    );
}

export default Transatcions;