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
    
    # Define a one-to-many relationship from Customer to Account
    accounts = relationship("Account", back_populates="customer")
    
    # Define a one-to-many relationship from Customer to Transaction
    transactions = relationship("Transaction", back_populates="customer")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.now)  # Use default=datetime.now
    description = Column(String)
    amount = Column(Float)
    account_id = Column(Integer, ForeignKey('accounts.id'))  # Add account_id
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    
    # Define a many-to-one relationship from Transaction to Account
    account = relationship("Account", back_populates="transactions")
    
    # Define a many-to-one relationship from Transaction to Customer
    customer = relationship("Customer", back_populates="transactions")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    account_type = Column(String)
    account_balance = Column(Float)
    customer_id = Column(Integer, ForeignKey('customers.id'))  # Add customer_id
    
    # Define a many-to-one relationship from Account to Customer
    customer = relationship("Customer", back_populates="accounts")
    
    # Define a one-to-many relationship from Account to Transaction
    transactions = relationship("Transaction", back_populates="account")
