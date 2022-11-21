from fastapi import APIRouter, HTTPException, status, Request
import requests
from data_base.bank_db_manager import bank_db_manager
from data_base.bank_db_manager import DBNoData
from routers.transactions_router_utils import *
from routers import Transaction
from json import JSONDecodeError
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/transaction/{user_id}", status_code=200)
def get_transactions_of_user(user_id):
    try:
        user_id = int(user_id)
        transactions = bank_db_manager.get_transactions_by_user_id(user_id)
        return transactions
    except DBNoData as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )


@router.post("/transaction/{user_id}", status_code=200)
async def add_transaction_to_user(user_id: str, request: Request):
    try:
        user_id = int(user_id)
        rawtransactionsDetails = await request.json()
        transaction = Transaction(**rawtransactionsDetails)
        result = bank_db_manager.add_transaction(
            user_id, transaction.category, transaction.amount, transaction.vendor)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exeception occured:{}".format(e))
    except (JSONDecodeError, KeyError) as ex:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"name": "Some Name", "town": "Some Town"})


@router.delete("/transaction/{transaction_id}", status_code=200)
def delete_transactoin_from_user(transaction_id):
    if not validate_transaction_id(transaction_id):
        raise HTTPException(status_code=400, detail="Wrong parameter")
    return bank_db_manager.delete_transaction(transaction_id)


@router.get("/transaction/breakdown/{user_id}", status_code=200)
def get_breakdown_for_user(user_id):
    try:
        user_id = int(user_id)
        raw_breakdown = bank_db_manager.get_breakdown_by_category(user_id)
        return raw_breakdown
    except DBNoData as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
