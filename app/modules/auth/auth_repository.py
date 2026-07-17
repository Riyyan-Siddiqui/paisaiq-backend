from sqlalchemy.orm import Session
from app.models.user import User

class AuthRepository:

    @staticmethod
    def find_by_email( email: str, db: Session):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def find_by_phone( phone: str, db: Session):
        return db.query(User).filter(User.phone == phone).first()
    

    @staticmethod
    def find_by_id(user_id , db: Session):
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def create_user(user: User, db: Session):
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def update_refresh_token(
        user: User,
        refresh_token: str,
        db: Session,
    ):
        user.refresh_token = refresh_token

        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def clear_refresh_token(
        user: User,
        db: Session,
    ):
        user.refresh_token = None

        db.commit()
        db.refresh(user)

    
    @staticmethod
    def update_password(
        user:User,
        hashed_password: str,
        db: Session,
    ):
        user.hashed_password = hashed_password

        db.commit()
        db.refresh(user)

    @staticmethod
    def verify_email(
        user: User,
        db: Session,
    ):
        
        user.is_email_verified = True

        db.commit()
        db.refresh(user)

        return user