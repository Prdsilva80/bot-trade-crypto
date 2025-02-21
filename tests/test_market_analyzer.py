# tests/test_market_analyzer.py
import pytest
import pandas as pd
import numpy as np
from trading_bot.market_analyzer import MarketAnalyzer

@pytest.fixture
def sample_data():
    # Cria dados de exemplo para testes
    data = {
        'timestamp': range(100),
        'open': np.random.random(100),
        'high': np.random.random(100),
        'low': np.random.random(100),
        'close': np.random.random(100),
        'volume': np.random.random(100),
        'close_time': range(100),
        'quote_volume': np.random.random(100),
        'trades': np.random.random(100),
        'taker_buy_base': np.random.random(100),
        'taker_buy_quote': np.random.random(100),
        'ignored': np.random.random(100)
    }
    return pd.DataFrame(data)

def test_market_analyzer_initialization():
    analyzer = MarketAnalyzer()
    assert analyzer is not None
    assert analyzer.scaler is not None
    assert analyzer.model is not None

def test_prepare_data(sample_data):
    analyzer = MarketAnalyzer()
    df = analyzer.prepare_data(sample_data.values.tolist())
    assert isinstance(df, pd.DataFrame)
    assert 'close' in df.columns
    assert df['close'].dtype == np.float64

def test_calculate_indicators(sample_data):
    analyzer = MarketAnalyzer()
    df = analyzer.calculate_indicators(sample_data)
    assert 'RSI' in df.columns
    assert 'MACD' in df.columns
    assert 'BB_upper' in df.columns
    assert 'BB_lower' in df.columns

def test_predict_market_movement(sample_data):
    analyzer = MarketAnalyzer()
    df = analyzer.calculate_indicators(sample_data)
    analysis = analyzer.predict_market_movement(df)
    assert isinstance(analysis, dict)
    assert 'RSI' in analysis
    assert 'MACD' in analysis
    assert 'Bollinger' in analysis
    assert 'tendencia' in analysis