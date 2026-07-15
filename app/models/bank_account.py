from datetime import datetime

from sqlalchemy import String, Float, Boolean, DateTime, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4

from app.database.database import Base


class bankAccount(Base):
    __tablename__ = "bank_accounts"

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id")
    )

    bank_name: Mapped[str] = mapped_column(String(100))

    account_title: Mapped[str] = mapped_column(String(150))

    account_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )

    account_type: Mapped[str] = mapped_column(String(30))

    current_balance: Mapped[float] = mapped_column(Float)

    currency: Mapped[str] = mapped_column(
        String(10),
        default="PKR",
    )

    is_primary: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    # Relationships
    user = relationship("User", back_populates="bank_accounts")

    transactions = relationship(
        "Transaction",
        back_populates="bank_account",
    )