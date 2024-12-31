# Configuration settings for the crypto tracker
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
CRYPTOCOMPARE_API_KEY = os.getenv('CRYPTOCOMPARE_API_KEY', '')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY', '')

# Supported networks and their configuration
NETWORKS = {
    'ethereum': {
        'api_url': 'https://api.etherscan.io/api',
        'explorer_url': 'https://etherscan.io',
        'symbol': 'ETH'
    },
    'binance': {
        'api_url': 'https://api.bscscan.com/api',
        'explorer_url': 'https://bscscan.com',
        'symbol': 'BNB'
    }
}

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///crypto_tracker.db')