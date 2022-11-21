import React, { useState, useEffect } from 'react';
import Header from './Header';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import '../styles/operations.css';
import axios from 'axios'

function Operations(props) {
    const categories = ["food", "clothes"];
    const [category, setCategory] = useState("")
    const [vendor, setVendor] = useState("")
    const [amount, setAmount] = useState("")

    const cleanInput = () => {
        setCategory("");
        setAmount("");
        setVendor("");
    }

    const addTransactions = async (amount) => {
        axios.post(`http://localhost:8000/transaction/${props.user.id}`,
            { "vendor": vendor, "amount": amount, "category": category })
            .then()
            .catch()
    }

    const addWithdraw = async () => {
        const amountToSubtract = parseInt(amount) * (-1);
        addTransactions(amountToSubtract)
            .then(
                cleanInput(),
                props.updateBalance(amountToSubtract)
            )
    }

    const addDeposit = async () => {
        addTransactions(amount)
            .then(
                cleanInput(),
                props.updateBalance(parseInt(amount))

            )
    }


    return (
        <div>
            <Header balance={props.user.balance}></Header>
            <div className='operations-container'>
                <Card className='operation-window' style={{ width: '18rem' }}>
                    <Card.Body>
                        <Card.Text>ADD TRANSACTION</Card.Text>
                        <Form.Control placeholder="Transaction vendor" value={vendor} onChange={event => { setVendor(event.target.value) }} />
                        <Form.Control placeholder="Transaction amount" value={amount} onChange={event => { setAmount(event.target.value) }} />
                        <Form.Select aria-label="Default select example" value={category} onChange={event => { setCategory(event.target.value) }}>
                            <option>Transaction category</option>
                            {categories.map((c, i) => <option key={i}>{c}</option>)}
                        </Form.Select>
                        <ButtonGroup aria-label="Basic example">
                            <Button variant="secondary" onClick={addWithdraw}>Withdraw</Button>
                            <Button variant="secondary" onClick={addDeposit}>deposit</Button>
                        </ButtonGroup>
                    </Card.Body>
                </Card>
            </div>
        </div>
    );
}

export default Operations;