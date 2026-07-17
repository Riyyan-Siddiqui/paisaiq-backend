import http

from fastapi import Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.database.dependency import get_db
from jose import jwt 
from app.modules.auth.auth_repository import AuthRepository
from app.core.security import verify_password

from app.core.config import JWT_ALGORITHM, JWT_SECRET



def get_current_user_refresh_token(
        request: Request,
        db: Session = Depends(get_db),
):
    refresh_token = request.cookies.get(
        "refresh_token"
    )

    if not refresh_token:
        raise HTTPException(
            status_code=401,
            detail="Refresh token missing.",
        )
    
    try:
        payload = jwt.decode(
            refresh_token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token.",
        )

    user_id = payload.get("sub")

    user = AuthRepository.find_by_id(
        user_id,
        db
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found."
        )
    
    if user.refresh_token is None:
        raise HTTPException(
            status_code=401,
            detail="Refresh token not found.",
        )

    matched_token = verify_password(refresh_token, user.refresh_token)

    if not matched_token:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token."
        )
    
    return user

