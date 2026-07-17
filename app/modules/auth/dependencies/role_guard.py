from fastapi import Depends, HTTPException

from app.modules.auth.dependencies.jwt_guard import (
    get_current_user,
)


def role_required(*roles):

    def dependency(
        current_user=Depends(
            get_current_user,
        )
    ):

        if current_user.role not in roles:
            raise HTTPException(
                status_code=403,
                detail="Forbidden.",
            )

        return current_user

    return dependency