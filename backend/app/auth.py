from passlib.context import CryptContext
from sqlalchemy.util import deprecated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)