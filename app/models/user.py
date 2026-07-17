from datetime import datetime

from sqlalchemy import Boolean, Enum, String, DateTime, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.enum import UserRole

from app.database.database import Base

from uuid import UUID, uuid4


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=True,
    )

    role: Mapped[str] = mapped_column(
        String(20),
        default=UserRole.USER.value
    )

    refresh_token: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    hashed_password: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    is_email_verified: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True
    )

    is_phone_verified: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True
    )


    # picture: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # currency: Mapped[str] = mapped_column(String(10), default="PKR")

    # language: Mapped[str] = mapped_column(String(20), default="en")

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    # Relationships
    bank_accounts = relationship("bankAccount", back_populates="user")

    # budgets = relationship("Budget", back_populates="user")

    # goals = relationship("Goal", back_populates="user")

    # bills = relationship("Bill", back_populates="user")

    # investments = relationship("Investment", back_populates="user")

    # notifications = relationship("Notification", back_populates="user")

    # conversations = relationship("Conversation", back_populates="user")

    # reports = relationship("WeeklyReport", back_populates="user")

    # saving_strategies = relationship(
    #     "SavingStrategy",
    #     back_populates="user",
    # )