from datetime import datetime

from sqlalchemy import (
    String,
    Float,
    Text,
    DateTime,
    ForeignKey,
    Uuid
)
from uuid import UUID, uuid4

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4
    )

    bank_account_id: Mapped[UUID] = mapped_column(
        ForeignKey("bank_accounts.id")
    )

    merchant: Mapped[str] = mapped_column(String(255))

    amount: Mapped[float] = mapped_column(Float)

    category: Mapped[str] = mapped_column(String(100))

    payment_method: Mapped[str] = mapped_column(String(50))

    type: Mapped[str] = mapped_column(String(20))

    date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Relationships
    bank_account = relationship(
        "bankAccount",
        back_populates="transactions",
    )

    # receipt = relationship(
    #     "Receipt",
    #     back_populates="transaction",
    #     uselist=False,
    # )

    # anomaly = relationship(
    #     "Anomaly",
    #     back_populates="transaction",
    #     uselist=False,
    # )