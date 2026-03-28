from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, EmailStr


# -----------------------------
# USER SCHEMAS
# -----------------------------

class UserCreate(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    address: str
    country: str
    state: str
    zip_code: str
    password: str


class UserResponse(BaseModel):
    id: str
    user_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    address: str
    country: str
    state: str
    zip_code: str

    class Config:
        from_attributes = True


# -----------------------------
# ACCOUNT SCHEMAS
# -----------------------------

class AccountCreate(BaseModel):
    user_id: str
    balance: Decimal = Decimal("0.00")
    currency: str
    account_type: str
    status: str = "active"


class AccountResponse(BaseModel):
    id: int
    user_db_id: str
    account_number: str
    balance: Decimal
    currency: str
    account_type: str
    status: str

    class Config:
        from_attributes = True


# -----------------------------
# CARD SCHEMAS
# -----------------------------

class CardCreate(BaseModel):
    account_id: int
    cardholder_name: str
    token: str | None = None
    last4: str
    card_type: str
    expiry_month: str
    expiry_year: str


class CardResponse(BaseModel):
    id: int
    account_id: int
    cardholder_name: str
    token: str | None = None
    last4: str
    card_type: str
    expiry_month: str
    expiry_year: str

    class Config:
        from_attributes = True


# -----------------------------
# TRANSACTION SCHEMAS
# -----------------------------

class TransactionCreate(BaseModel):
    account_id: int
    card_id: int | None = None
    amount: Decimal
    currency: str
    type: str
    source_type: str
    description: str | None = None


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    card_id: int | None = None
    amount: Decimal
    currency: str
    type: str
    source_type: str
    description: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True