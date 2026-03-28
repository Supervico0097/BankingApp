from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
import random

from app.auth import hash_password
from app.database import get_db
from app.models import User, Account
from app.schemas import AccountCreate, AccountResponse

def generate_account_number(db: Session) -> str:

    while True:
        account_number = "4503" + "".join(str(random.randint(0,9)) for _ in range(8))

        existing_account = db.query(Account).filter(Account.account_number == account_number).first()

        if not existing_account:
            return account_number

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post(path="/add", response_model=AccountResponse)
def add_account(account: AccountCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == account.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_account = Account(
        user_db_id = db.query(User).filter(User.user_id == account.user_id).first().id,
        account_number = generate_account_number(db),
        balance = 0,
        currency = account.currency,
        account_type  = account.account_type,
        status = "active"
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account





