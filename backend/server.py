from asyncio import events
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from routers import transactions_router, users_router
from data_base.bank_db_manager import Bank_DB_Manager

app = FastAPI()
app.include_router(transactions_router.router)
app.include_router(users_router.router)

bank_db_manager = Bank_DB_Manager()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sanity")
def root():
    return {"message": "Server is running"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
