from binance.client import Client

class BinanceHandler:
    def __init__(self):
        # Inicializa o cliente sem autenticação para endpoints públicos
        self.client = Client()
    
    def get_symbol_price(self, symbol):
        """Obtém o preço atual de um par de trading"""
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except Exception as e:
            print(f"Erro ao obter preço: {str(e)}")
            return None
    
    def get_market_data(self, symbol, interval='1h', limit=100):
        """Obtém dados históricos do mercado"""
        try:
            klines = self.client.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit
            )
            return klines
        except Exception as e:
            print(f"Erro ao obter dados do mercado: {str(e)}")
            return None