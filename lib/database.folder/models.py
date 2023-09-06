from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float, create_engine, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.now)  # Use default=datetime.now
    description = Column(String)
    amount = Column(Float)
    
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    account_type = Column(String)
    account_balance = Column(Float)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
