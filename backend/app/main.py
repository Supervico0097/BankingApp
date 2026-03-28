from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import users, accounts

Base.metadata.create_all(bind=engine)

app = FastAPI(title="VX Banking Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

app.include_router(users.router)
app.include_router(accounts.router)
