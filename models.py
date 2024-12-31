from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallets'
    
    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True, nullable=False)
    label = Column(String)
    network = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    balances = relationship("Balance", back_populates="wallet")

class Balance(Base):
    __tablename__ = 'balances'
    
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    token_symbol = Column(String, nullable=False)
    amount = Column(Float)
    usd_value = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow)
    wallet = relationship("Wallet", back_populates="balances")

def init_db(database_url):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return engine