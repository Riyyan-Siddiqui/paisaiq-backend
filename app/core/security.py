from uuid import UUID

from pwdlib import PasswordHash
from jose import jwt
from datetime import datetime, timedelta, timezone

from app.core.config import ACCESS_TOKEN_EXPIRES_IN, REFRESH_TOKEN_EXPIRES_IN, JWT_ALGORITHM, JWT_SECRET

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

def create_access_token(user_id: UUID):

    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=int(ACCESS_TOKEN_EXPIRES_IN)),
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )


def create_refresh_token(user_id: UUID):

    payload = {
        # UUID() expects a hex/str or int via the 'int' keyword
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc)
        + timedelta(days=int(REFRESH_TOKEN_EXPIRES_IN)),
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
def decode_token():
    return 