import React from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import '../styles/transaction.css'


function Transaction(props) {
    const transaction = props.transaction;
    const t_type = transaction.amount <= 0 ? "withdraw": "depoist";
    const amountAbs = Math.abs(parseInt(transaction.amount))

    const deleteTransaction = () => {
        props.deleteTransaction(transaction.id);
        props.updateBalance(transaction.amount * (-1));
    }
    return (
     
        <Card className='transaction-card' style={{ width: '18rem' }}>
            <Card.Body className={t_type}>
              <Card.Title>{transaction.vendor}</Card.Title>
              <Card.Text> {transaction.category}</Card.Text>
              <Card.Text>{amountAbs}</Card.Text>
              <Button variant="primary" onClick={deleteTransaction}>Delete</Button>
            </Card.Body>
        </Card>
    );
}

export default Transaction;