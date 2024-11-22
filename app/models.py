from sqlalchemy import CheckConstraint, Column, Integer, String

from app.database import Base


class Product(Base):
    __tablename__ = 'tb_product'
    __table_args__ = (
        CheckConstraint('price >= 0', name='ck_price_non_negative'),
        # {'schema': 'public'}
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
