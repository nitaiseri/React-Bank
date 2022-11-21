from pydantic import BaseModel, ValidationError
 
class Transaction(BaseModel):
    transaction_id: int = -1
    amount: float
    vendor: str
    category: str