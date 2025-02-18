import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

class MarketAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    def prepare_data(self, klines):
        """Prepara os dados do mercado para análise"""
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 
            'volume', 'close_time', 'quote_volume', 'trades',
            'taker_buy_base', 'taker_buy_quote', 'ignored'
        ])
        
        # Converte valores para numérico
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = pd.to_numeric(df[col])
        
        return df
    
    def calculate_indicators(self, df):
        """Calcula indicadores técnicos"""
        try:
            # Média Móvel Simples de 20 períodos
            df['SMA_20'] = df['close'].rolling(window=20).mean()
            
            # RSI - Relative Strength Index
            delta = df['close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['RSI'] = 100 - (100 / (1 + rs))
            
            # Bollinger Bands
            df['BB_middle'] = df['close'].rolling(window=20).mean()
            df['BB_upper'] = df['BB_middle'] + 2 * df['close'].rolling(window=20).std()
            df['BB_lower'] = df['BB_middle'] - 2 * df['close'].rolling(window=20).std()
            
            # MACD
            exp1 = df['close'].ewm(span=12, adjust=False).mean()
            exp2 = df['close'].ewm(span=26, adjust=False).mean()
            df['MACD'] = exp1 - exp2
            df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
            
            return df
        except Exception as e:
            print(f"Erro ao calcular indicadores: {str(e)}")
            return df

    def predict_market_movement(self, df):
        """Analisa o mercado usando indicadores técnicos"""
        try:
            last_row = df.iloc[-1]
            
            analysis = {
                'RSI': {
                    'valor': last_row['RSI'],
                    'sinal': 'Sobrecomprado' if last_row['RSI'] > 70 else 'Sobrevendido' if last_row['RSI'] < 30 else 'Neutro'
                },
                'MACD': {
                    'valor': last_row['MACD'],
                    'sinal': 'Compra' if last_row['MACD'] > last_row['Signal_Line'] else 'Venda'
                },
                'Bollinger': {
                    'superior': last_row['BB_upper'],
                    'meio': last_row['BB_middle'],
                    'inferior': last_row['BB_lower'],
                    'sinal': 'Sobrecomprado' if last_row['close'] > last_row['BB_upper'] else 'Sobrevendido' if last_row['close'] < last_row['BB_lower'] else 'Neutro'
                },
                'tendencia': 'ALTA' if last_row['close'] > last_row['SMA_20'] else 'BAIXA'
            }
            
            return analysis
        except Exception as e:
            print(f"Erro na análise de mercado: {str(e)}")
            return None