# Crypto Portfolio Tracker

A FastAPI-based application that tracks crypto wallet balances across different networks and calculates portfolio value.

## Features

- Track multiple wallet addresses across different networks (Ethereum, Binance Smart Chain)
- Get real-time wallet balances
- Calculate total portfolio value in USD
- Store historical balance data
- RESTful API interface

## Setup

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

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your API keys:
```
CRYPTOCOMPARE_API_KEY=your_cryptocompare_api_key
ETHERSCAN_API_KEY=your_etherscan_api_key
DATABASE_URL=sqlite:///crypto_tracker.db
```
(If you're on Windows and don't know how to operate environment variables, just modify them in the config.py file)

5. Run the application
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

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

## Project Structure

- `main.py`: FastAPI application and routes
- `config.py`: Configuration settings and API keys
- `models.py`: SQLAlchemy database models
- `wallet_service.py`: Core business logic for wallet tracking
- `requirements.txt`: Project dependencies

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License - feel free to use this project for your own purposes.
