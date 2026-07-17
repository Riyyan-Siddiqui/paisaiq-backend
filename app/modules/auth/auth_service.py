from app.modules.auth.auth_repository import AuthRepository
from app.core.security import hash_password, create_access_token, create_refresh_token, verify_password
from fastapi import HTTPException
from app.models.user import User

class AuthService:
    @staticmethod
    def signup(data, res, db):
        try:

            # Check if user already exists
            if (data.email is not None):
                existing_user = AuthRepository.find_by_email(
                    data.email,
                    db,
                )
            elif(data.phone is not None):
                existing_user = AuthRepository.find_by_phone(
                    data.phone,
                    db,
                )

            if existing_user:
                raise HTTPException(
                    status_code=400,
                    detail="User already exists.",
                )

            # Hash password
            hashed_password = hash_password(data.password)

            # Create user model
            user = User(
                name=data.name,
                email=data.email,
                phone=data.phone,
                hashed_password=hashed_password,
            )

            # Save user
            user = AuthRepository.create_user(user, db)

            # Generate JWTs
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)

            # Hash refresh token before saving
            hashed_refresh_token = hash_password(refresh_token)

            # Save refresh token
            AuthRepository.update_refresh_token(
                user,
                hashed_refresh_token,
                db,
            )

            res.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=900,
            )


            res.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=604800,
            )

            return {
                "message": "User registered successfully.",
                "user": {
                    "id": str(user.id),
                    "name": user.name,
                    "email": user.email,
                    "phone": user.phone,
                }
            }

        except HTTPException:
            raise

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e),
            )
    
    @staticmethod
    def signin(data,res, db):
        # Check if the user exists
        if (data.email is not None):
                existing_user = AuthRepository.find_by_email(
                    data.email,
                    db,
                )
        elif(data.phone is not None):
            existing_user = AuthRepository.find_by_phone(
                data.phone,
                db,
            )

        if existing_user is None:
            raise HTTPException(
                status_code=400,
                detail="User does not exist. Try signing up.",
            )

        # verify password

        if existing_user.hashed_password is None:
            raise HTTPException(
                status_code=400,
                detail="Password field is empty! Please sign in using Google",
            )

        matched_password = verify_password(data.password, existing_user.hashed_password )
        if not matched_password:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials.",
            )

        # generate access token
        access_token = create_access_token(existing_user.id)

        # generate refresh token
        refresh_token = create_refresh_token(existing_user.id)

        # hash refresh token
        hashed_refresh_token = hash_password(refresh_token)

        # save refresh token in the database
        AuthRepository.update_refresh_token(
            existing_user,
            hashed_refresh_token,
            db
        )
        # response access token in httpCookie
        res.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=900,
            )


        # response refresh token in httpCookie
        res.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=604800,
            )

        # return message
        return {
                "message": "Signed in successfully.",
                "user": {
                    "id": str(existing_user.id),
                    "name": existing_user.name,
                    "email": existing_user.email,
                }
            }


    @staticmethod
    def refresh(res, current_user):


        access_token = create_access_token(
            current_user.id
        )

        res.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="none",
            max_age=900,
        )

        return {
            "message": "Token refreshed."
        }
    
    @staticmethod
    def logout(res):
        res.delete_cookie(
            "access_token"
        )

        res.delete_cookie(
            "refresh_token"
        )

        return {
            "message": "Logged out."
        }