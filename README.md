# Crypto Portfolio Tracker

Simpler version that is a lot easier to install and use (and has a CLI): https://github.com/JustLeska/simple-crypto-portfolio-tracker

---

A full-stack application that tracks crypto wallet balances across different networks and calculates portfolio value, thanks to a FastAPI backend ~~and a React frontend~~ (discontinued here to be perfected in final version).

**DISCLAMER:** This is mainly an educational project to train me in the coding space & maybe help others, so this is not intended for a real use.
**TL;DR:** things might break :P

## Features

- Track multiple wallet addresses across different networks (Ethereum, Binance Smart Chain)
- Real-time wallet balance updates
- Calculate total portfolio value in USD
- RESTful API backend

## Prerequisites

- Python 3.8 or higher
- CryptoCompare API key (for price data)
- Etherscan API key (for Ethereum blockchain data)

## Project Structure

```
crypto-portfolio-tracker/
├── backend/
│   ├── config.py
│   ├── models.py
│   ├── wallet_service.py
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## Setup Instructions

### Backend Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/crypto-portfolio-tracker.git
cd crypto-portfolio-tracker
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory with your API keys:
```
CRYPTOCOMPARE_API_KEY=your_cryptocompare_api_key
ETHERSCAN_API_KEY=your_etherscan_api_key
DATABASE_URL=sqlite:///crypto_tracker.db
```
(If you're on Windows and don't know how to operate environment variables, just add the keys and database URL in the config.py file)

### Run Backend

Backend:
```bash
cd backend
uvicorn main:app --reload
```

The application will be available at:

- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Using the API Endpoints

### Add a new wallet
```
POST /wallets/
{
    "address": "0x...",
    "network": "ethereum",
    "label": "My Main Wallet"
}
```

### Get wallet balance
```
GET /wallets/{wallet_id}/balance
```

### Get portfolio summary
```
GET /portfolio
```

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License - feel free to use this project for your own purposes.
