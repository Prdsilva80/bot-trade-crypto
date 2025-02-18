from flask import Flask, jsonify, render_template
from trading_bot.binance_client import BinanceHandler
from trading_bot.market_analyzer import MarketAnalyzer

app = Flask(__name__)

binance = BinanceHandler()
analyzer = MarketAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price/<symbol>')
def get_price(symbol):
    price = binance.get_symbol_price(symbol)
    if price:
        return jsonify({
            'status': 'success',
            'symbol': symbol,
            'price': price
        })
    return jsonify({
        'status': 'error',
        'message': 'Erro ao obter preço'
    })

@app.route('/analyze/<symbol>')
def analyze_market(symbol):
    try:
        # Obtém dados do mercado
        klines = binance.get_market_data(symbol)
        if not klines:
            return jsonify({
                'status': 'error',
                'message': 'Falha ao obter dados do mercado'
            })
        
        # Prepara e analisa os dados
        df = analyzer.prepare_data(klines)
        df = analyzer.calculate_indicators(df)
        
        # Obtém análise técnica
        analysis = analyzer.predict_market_movement(df)
        
        if analysis:
            return jsonify({
                'status': 'success',
                'symbol': symbol,
                'analysis': analysis
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Falha na análise'
            })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erro: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True)