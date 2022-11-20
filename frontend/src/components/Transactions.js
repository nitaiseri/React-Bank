import React from 'react';
import Transaction from './Transaction';

function Transatcions(props) {

    const [transactions, setTransactions] = useState([])

    return (
        <div className='transactions-container'>
            {transactions.map((t, k) => <Transaction key={k} transaction={t}></Transaction>)}
        </div>
    );
}

export default Transatcions;