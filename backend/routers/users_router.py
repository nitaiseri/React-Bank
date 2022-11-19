from fastapi import APIRouter, HTTPException, status
import requests
from data_base.bank_db_manager import bank_db_manager
from data_base.bank_db_manager import DBNoData

router = APIRouter()

@router.get("/user/balance/{user_id}", status_code=200)
def get_balance_of_user(user_id):
    try:
        balance = bank_db_manager.get_balance_of_user(user_id)  
        return balance

    except DBNoData as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
