# Crypto Portfolio Tracker

A full-stack application that tracks crypto wallet balances across different networks and calculates portfolio value, thanks to both a FastAPI backend and a React frontend.

**DISCLAMER:** This is mainly an educational project to train me in the coding space & maybe help others, so this is not intended for a real use.
**TL;DR:** things might break :P

## Features

- Track multiple wallet addresses across different networks (Ethereum, Binance Smart Chain)
- Real-time wallet balance updates
- Calculate total portfolio value in USD
- Store historical balance data
- Modern React frontend interface
- RESTful API backend

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
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

1. In a new terminal, set up the frontend:
```bash
# Create and setup the frontend
npm create vite@latest frontend -- --template react
cd frontend
```

2. Install required dependencies:
```bash
npm install lucide-react
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

3. Start the frontend development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:5173

### Run Frontend and Backend

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

## Usage

1. Ensure both backend and frontend servers are running
2. Visit http://localhost:5173 in your browser
3. Use the "Add New Wallet" form to add wallet addresses:
   - Enter the wallet address
   - Select the network (Ethereum or BSC)
   - Optionally add a label
4. View your portfolio summary and individual wallet balances
5. Use the refresh button to update balances

## Common Issues & Solutions

1. **Default Vite Page Shows**: Make sure you've replaced all the default Vite files with our crypto tracker code.
2. **Backend Connection Error**: Ensure the backend server is running on port 8000 and CORS is properly configured.
3. **Missing Dependencies**: Run `npm install` in the frontend directory to install all required dependencies.

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License - feel free to use this project for your own purposes.
