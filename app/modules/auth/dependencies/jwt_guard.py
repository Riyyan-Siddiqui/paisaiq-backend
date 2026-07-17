import http
from webbrowser import get

from fastapi import Depends, HTTPException, Request
from jose import jwt 
from sqlalchemy.orm import Session


from app.database.dependency import get_db
from app.modules.auth.auth_repository import AuthRepository
from app.core.config import JWT_SECRET, JWT_ALGORITHM

def get_current_user(
        request: Request, 
        db: Session = Depends(get_db)
):
    access_token = request.cookies.get("access_token")

    if not access_token:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized."
        )

    payload = jwt.decode(
        access_token,
        JWT_SECRET,
        algorithms=JWT_ALGORITHM
    )

    user_id = payload.get("sub")
    print(type(user_id))

    user = AuthRepository.find_by_id(
        user_id,
        db
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found."
        )
    return user
