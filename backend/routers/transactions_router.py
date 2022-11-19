from fastapi import APIRouter, HTTPException, status
import requests
from data_base.bank_db_manager import bank_db_manager

router = APIRouter()

@router.get("/transaction/{user_id}", status_code=200)
def get_balance_of_user(user_id):
    pass

@router.post("/transaction/{user_id}", status_code=200)
def add_transaction_to_user(user_id):
    pass

@router.delete("/transaction/{user_id}", status_code=200)
def delete_transactoin_from_user(user_id):
    pass

@router.get("/transaction/breakdown/{user_id}", status_code=200)
def get_breakdown_for_user(user_id):
    pass