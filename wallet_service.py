import requests
from datetime import datetime
from typing import Dict, List
from sqlalchemy.orm import Session
from models import Wallet, Balance
from config import NETWORKS, CRYPTOCOMPARE_API_KEY, ETHERSCAN_API_KEY

class WalletService:
    def __init__(self, session: Session):
        self.session = session
        
    def add_wallet(self, address: str, network: str, label: str = None) -> Wallet:
        """Add a new wallet to track"""
        wallet = Wallet(address=address, network=network, label=label)
        self.session.add(wallet)
        self.session.commit()
        return wallet
    
    def get_address_balance(self, address: str, network: str) -> Dict:
        """Get the native token balance for a given address"""
        network_config = NETWORKS.get(network.lower())
        if not network_config:
            raise ValueError(f"Unsupported network: {network}")
            
        params = {
            'module': 'account',
            'action': 'balance',
            'address': address,
            'apikey': ETHERSCAN_API_KEY
        }
        
        response = requests.get(network_config['api_url'], params=params)
        data = response.json()
        
        if data['status'] != '1':
            raise Exception(f"API Error: {data.get('message', 'Unknown error')}")
            
        balance_wei = int(data['result'])
        balance_eth = balance_wei / 1e18  # Convert from wei to ETH
        
        return {
            'address': address,
            'network': network,
            'symbol': network_config['symbol'],
            'balance': balance_eth
        }
    
    def get_token_prices(self, symbols: List[str]) -> Dict:
        """Get current prices for multiple tokens"""
        symbols_str = ','.join(symbols)
        url = f"https://min-api.cryptocompare.com/data/pricemulti"
        params = {
            'fsyms': symbols_str,
            'tsyms': 'USD',
            'api_key': CRYPTOCOMPARE_API_KEY
        }
        
        response = requests.get(url, params=params)
        return response.json()
    
    def update_wallet_balances(self, wallet_id: int):
        """Update balances for a specific wallet"""
        wallet = self.session.query(Wallet).get(wallet_id)
        if not wallet:
            raise ValueError(f"Wallet not found: {wallet_id}")
            
        # Get native token balance
        balance_info = self.get_address_balance(wallet.address, wallet.network)
        
        # Get current price
        prices = self.get_token_prices([balance_info['symbol']])
        usd_price = prices.get(balance_info['symbol'], {}).get('USD', 0)
        
        # Update or create balance record
        balance = self.session.query(Balance).filter_by(
            wallet_id=wallet.id,
            token_symbol=balance_info['symbol']
        ).first()
        
        if not balance:
            balance = Balance(wallet_id=wallet.id, token_symbol=balance_info['symbol'])
            self.session.add(balance)
        
        balance.amount = balance_info['balance']
        balance.usd_value = balance.amount * usd_price
        balance.last_updated = datetime.utcnow()
        
        self.session.commit()
        return balance
    
    def get_portfolio_value(self) -> Dict:
        """Calculate total portfolio value across all wallets"""
        total_value = 0
        portfolio = []
        
        wallets = self.session.query(Wallet).all()
        for wallet in wallets:
            wallet_value = 0
            wallet_balances = []
            
            for balance in wallet.balances:
                wallet_value += balance.usd_value
                wallet_balances.append({
                    'token': balance.token_symbol,
                    'amount': balance.amount,
                    'usd_value': balance.usd_value
                })
            
            portfolio.append({
                'address': wallet.address,
                'network': wallet.network,
                'label': wallet.label,
                'balances': wallet_balances,
                'total_value': wallet_value
            })
            total_value += wallet_value
        
        return {
            'wallets': portfolio,
            'total_value': total_value
        }
