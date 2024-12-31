from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import Optional
from models import init_db
from wallet_service import WalletService
from config import DATABASE_URL

app = FastAPI(title="Crypto Portfolio Tracker")

# Initialize database
engine = init_db(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class WalletCreate(BaseModel):
    address: str
    network: str
    label: Optional[str] = None

@app.post("/wallets/")
async def add_wallet(wallet: WalletCreate):
    """Add a new wallet to track"""
    session = SessionLocal()
    try:
        service = WalletService(session)
        new_wallet = service.add_wallet(wallet.address, wallet.network, wallet.label)
        return {"id": new_wallet.id, "address": new_wallet.address}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@app.get("/wallets/{wallet_id}/balance")
async def get_wallet_balance(wallet_id: int):
    """Get current balance for a specific wallet"""
    session = SessionLocal()
    try:
        service = WalletService(session)
        balance = service.update_wallet_balances(wallet_id)
        return {
            "token": balance.token_symbol,
            "amount": balance.amount,
            "usd_value": balance.usd_value,
            "last_updated": balance.last_updated
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@app.get("/portfolio")
async def get_portfolio():
    """Get total portfolio value and breakdown"""
    session = SessionLocal()
    try:
        service = WalletService(session)
        return service.get_portfolio_value()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()