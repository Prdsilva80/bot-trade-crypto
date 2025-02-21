# tests/test_binance_client.py
import pytest
from trading_bot.binance_client import BinanceHandler

def test_binance_handler_initialization():
    handler = BinanceHandler()
    assert handler is not None

def test_get_symbol_price():
    handler = BinanceHandler()
    price = handler.get_symbol_price('BTCUSDT')
    assert isinstance(price, float)
    assert price > 0

def test_get_market_data():
    handler = BinanceHandler()
    klines = handler.get_market_data('BTCUSDT')
    assert isinstance(klines, list)
    assert len(klines) > 0
    assert len(klines[0]) == 12  # Verifica se tem todas as colunas esperadas