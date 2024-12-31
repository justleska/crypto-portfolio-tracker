# Crypto Portfolio Tracker

A full-stack application that tracks crypto wallet balances across different networks and calculates portfolio value, featuring both a FastAPI backend and a React frontend.

## Features

- Track multiple wallet addresses across different networks (Ethereum, Binance Smart Chain)
- Real-time wallet balance updates
- Calculate total portfolio value in USD
- Store historical balance data
- Modern React frontend interface
- RESTful API backend

## Project Structure

```
crypto-portfolio-tracker/
├── backend/
│   ├── config.py
│   ├── models.py
│   ├── wallet_service.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── CryptoPortfolio.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── index.html
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

### Frontend Setup

0. Download Node.js and NPM if not done already: [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

1. Create a new React project using Vite
```bash
npm create vite@latest frontend -- --template react
cd frontend
```

2. Install frontend dependencies
```bash
npm install @shadcn/ui lucide-react
```

3. Install and configure Tailwind CSS (required for shadcn/ui)
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

4. Run both applications

Backend:
```bash
cd backend
uvicorn main:app --reload
```

Frontend:
```bash
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:5173
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

## Using the Frontend Interface

1. Visit http://localhost:5173 in your browser
2. Use the "Add New Wallet" form to add wallet addresses
3. View your portfolio summary and individual wallet balances
4. Click the refresh button to update balances

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License - feel free to use this project for your own purposes.
