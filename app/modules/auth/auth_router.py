from fastapi import Response

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.modules.auth.auth_service import AuthService
from app.modules.auth.auth_schema import SignupDto, SigninDto
from app.modules.auth.dependencies.refresh_guard import get_current_user_refresh_token

router = APIRouter(prefix='/v1/auth', tags=["Auth"])

@router.post("/signup") 
def signup(
    data: SignupDto,
    res: Response,
    db: Session = Depends(get_db)
):
    try:

        if not data.email and not data.phone:
            raise HTTPException(
                status_code=400,
                detail="Email or phone number is required."
            )
        return AuthService.signup(data,res, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
    
@router.post("/signin")
def signin(
    data: SigninDto,
    res: Response,
    db: Session = Depends(get_db)
):
    try:
        if not data.email and not data.phone:
            raise HTTPException(
                status_code=400,
                detail="Email or phone number is required."
            )
        return AuthService.signin(data, res, db)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
    
@router.post("/refresh")
def refresh(
    res: Response,
    current_user = Depends(get_current_user_refresh_token),
):
    return AuthService.refresh(res, current_user)


@router.post("/logout")
def logout(
    res: Response
):
    return AuthService.logout(res)
    