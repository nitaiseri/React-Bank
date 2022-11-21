from pydantic import BaseModel, ValidationError
 
class Transaction(BaseModel):
    transaction_id: int
    amount: float
    vendor: str
    category: str