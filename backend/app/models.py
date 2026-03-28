import uuid
from datetime import datetime
from sqlalchemy import Numeric

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, unique=True, index=True, nullable=False)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    country = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    accounts = relationship("Account", back_populates="user", cascade="all, delete-orphan")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_db_id = Column(String, ForeignKey("users.id"), nullable=False)

    account_number = Column(String, unique=True, index=True, nullable=False)
    balance = Column(Numeric(18,2), default=0.0, nullable=False)
    currency = Column(String, nullable=False)
    account_type = Column(String, nullable=False)
    status = Column(String, default="active", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="accounts")
    cards = relationship("Card", back_populates="account", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    cardholder_name = Column(String, nullable=False)
    token = Column(String, unique=True, index=True, nullable=True)
    last4 = Column(String(4), nullable=False)
    expiry_month = Column(String, nullable=False)
    expiry_year = Column(String, nullable=False)
    card_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    account = relationship("Account", back_populates="cards")
    transactions = relationship("Transaction", back_populates="card")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=True)

    amount = Column(Numeric(18,2), nullable=False)
    currency = Column(String, nullable=False)
    type = Column(String, nullable=False)  # debit / credit
    source_type = Column(String, nullable=False)  # card / transfer / atm / incoming_transfer
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    account = relationship("Account", back_populates="transactions")
    card = relationship("Card", back_populates="transactions")