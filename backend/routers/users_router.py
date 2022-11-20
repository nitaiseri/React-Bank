from fastapi import APIRouter, HTTPException, status
import requests
from data_base.bank_db_manager import bank_db_manager
from data_base.bank_db_manager import DBNoData

router = APIRouter()

@router.get("/user/{user_id}", status_code=200)
def get_user_info(user_id):
    try:
        user_id = int(user_id)
        userInfo = bank_db_manager.get_user_info(user_id)  
        return userInfo

    except DBNoData as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )

@router.get("/user/balance/{user_id}", status_code=200)
def get_balance_of_user(user_id):
    try:
        user_id = int(user_id)
        balance = bank_db_manager.get_balance_of_user(user_id)  
        return balance

    except DBNoData as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
