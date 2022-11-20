import Transaction from './Transaction';
import React, { useState, useEffect } from 'react';
import Header from './Header';



function Transatcions(props) {
    const [transactions, setTransactions] = useState([])

    return (
        <div className='transactions-container'>
            <Header userId={props.userId}></Header>
            Transactions
            {transactions.map((t, k) => <Transaction key={k} transaction={t}></Transaction>)}
        </div>
    );
}

export default Transatcions;