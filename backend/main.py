from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import Optional
from models import init_db
from wallet_service import WalletService
from config import DATABASE_URL

app = FastAPI(
    title="Crypto Portfolio Tracker",
    description="Track crypto wallet balances and portfolio values across different networks",
    version="1.0.0"
)

# Initialize database
engine = init_db(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class WalletCreate(BaseModel):
    address: str
    network: str
    label: Optional[str] = None

@app.get("/", response_class=HTMLResponse)
async def root():
    """Home page with API documentation"""
    return """
    <html>
        <head>
            <title>Crypto Portfolio Tracker</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                h1 { color: #333; }
                .endpoint { background: #f4f4f4; padding: 10px; margin: 10px 0; border-radius: 5px; }
                code { background: #e0e0e0; padding: 2px 5px; border-radius: 3px; }
            </style>
        </head>
        <body>
            <h1>Crypto Portfolio Tracker API</h1>
            <p>Welcome to the Crypto Portfolio Tracker API. Available endpoints:</p>
            
            <div class="endpoint">
                <h3>📝 Add New Wallet</h3>
                <code>POST /wallets/</code>
                <p>Add a new wallet address to track.</p>
            </div>
            
            <div class="endpoint">
                <h3>💰 Get Wallet Balance</h3>
                <code>GET /wallets/{wallet_id}/balance</code>
                <p>Get current balance for a specific wallet.</p>
            </div>
            
            <div class="endpoint">
                <h3>📊 View Portfolio</h3>
                <code>GET /portfolio</code>
                <p>Get total portfolio value and breakdown.</p>
            </div>
            
            <p>For detailed API documentation, visit <a href="/docs">/docs</a></p>
        </body>
    </html>
    """

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
