from asyncio import events
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from routers import transactions_router, users_router
from data_base.bank_db_manager import bank_db_manager

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
app.include_router(transactions_router.router)
app.include_router(users_router.router)
origins = [
    "http://localhost",
    "http://localhost:3000",
]


@app.get("/sanity")
def root():
    return {"message": "Server is running"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
