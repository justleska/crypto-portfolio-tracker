import { useState, useEffect } from 'react';
import { PlusCircle, Wallet, RefreshCw, DollarSign } from 'lucide-react';
import { Alert, AlertDescription } from '@/components/ui/alert';

export default function CryptoPortfolio() {
  const [wallets, setWallets] = useState([]);
  const [portfolio, setPortfolio] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [newWallet, setNewWallet] = useState({
    address: '',
    network: 'ethereum',
    label: ''
  });

  const fetchPortfolio = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:8000/portfolio');
      const data = await response.json();
      setPortfolio(data);
      setError('');
    } catch (err) {
      setError('Failed to fetch portfolio data');
    } finally {
      setLoading(false);
    }
  };

  const addWallet = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const response = await fetch('http://localhost:8000/wallets/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newWallet)
      });
      
      if (!response.ok) throw new Error('Failed to add wallet');
      
      setNewWallet({ address: '', network: 'ethereum', label: '' });
      fetchPortfolio();
    } catch (err) {
      setError('Failed to add wallet');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPortfolio();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold text-gray-900">Crypto Portfolio Tracker</h1>
          <button 
            onClick={fetchPortfolio}
            className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
            disabled={loading}
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            Refresh
          </button>
        </div>

        {/* Error Alert */}
        {error && (
          <Alert variant="destructive">
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {/* Add Wallet Form */}
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <PlusCircle className="w-5 h-5" />
            Add New Wallet
          </h2>
          <form onSubmit={addWallet} className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <input
                type="text"
                placeholder="Wallet Address"
                value={newWallet.address}
                onChange={(e) => setNewWallet({...newWallet, address: e.target.value})}
                className="p-2 border rounded"
                required
              />
              <select
                value={newWallet.network}
                onChange={(e) => setNewWallet({...newWallet, network: e.target.value})}
                className="p-2 border rounded"
              >
                <option value="ethereum">Ethereum</option>
                <option value="binance">Binance Smart Chain</option>
              </select>
              <input
                type="text"
                placeholder="Label (optional)"
                value={newWallet.label}
                onChange={(e) => setNewWallet({...newWallet, label: e.target.value})}
                className="p-2 border rounded"
              />
            </div>
            <button
              type="submit"
              className="w-full px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
              disabled={loading}
            >
              Add Wallet
            </button>
          </form>
        </div>

        {/* Portfolio Summary */}
        {portfolio && (
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold flex items-center gap-2">
                <Wallet className="w-5 h-5" />
                Portfolio Summary
              </h2>
              <div className="flex items-center gap-2 text-xl font-bold text-green-600">
                <DollarSign className="w-5 h-5" />
                {portfolio.total_value.toLocaleString('en-US', {
                  style: 'currency',
                  currency: 'USD'
                })}
              </div>
            </div>
            
            <div className="space-y-4">
              {portfolio.wallets.map((wallet, index) => (
                <div key={index} className="border rounded-lg p-4">
                  <div className="flex justify-between items-center mb-2">
                    <div>
                      <h3 className="font-semibold">{wallet.label || 'Unnamed Wallet'}</h3>
                      <p className="text-sm text-gray-500">{wallet.address}</p>
                    </div>
                    <span className="font-semibold text-green-600">
                      {wallet.total_value.toLocaleString('en-US', {
                        style: 'currency',
                        currency: 'USD'
                      })}
                    </span>
                  </div>
                  <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mt-2">
                    {wallet.balances.map((balance, idx) => (
                      <div key={idx} className="bg-gray-50 p-2 rounded">
                        <div className="text-sm text-gray-600">{balance.token}</div>
                        <div className="font-medium">{balance.amount.toFixed(4)}</div>
                        <div className="text-sm text-gray-500">
                          {balance.usd_value.toLocaleString('en-US', {
                            style: 'currency',
                            currency: 'USD'
                          })}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}