from flask import Flask, jsonify, render_template
from trading_bot.binance_client import BinanceHandler
from trading_bot.market_analyzer import MarketAnalyzer
import pandas as pd

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
        print(f"Analisando mercado para {symbol}")
        # Obtém dados do mercado
        klines = binance.get_market_data(symbol)
        print(f"Dados recebidos da Binance: {len(klines) if klines else 'Nenhum'} registros")
        
        if not klines:
            return jsonify({
                'status': 'error',
                'message': 'Falha ao obter dados do mercado'
            })
        
        # Prepara e analisa os dados
        print("Preparando dados...")
        df = analyzer.prepare_data(klines)
        print(f"DataFrame criado com {len(df)} linhas")
        
        print("Calculando indicadores...")
        df = analyzer.calculate_indicators(df)
        print("Indicadores calculados")
        
        # Obtém análise técnica
        print("Iniciando análise técnica...")
        analysis = analyzer.predict_market_movement(df)
        print(f"Análise concluída: {analysis is not None}")
        
        # Prepara dados para os gráficos
        print("Preparando dados para os gráficos...")
        try:
            # Converte timestamp para datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            print("Timestamp convertido")
            
            # Pega os últimos 100 registros
            last_100 = df.tail(100)
            print(f"Selecionados últimos {len(last_100)} registros")
            
            # Substitui valores NaN por None para JSON válido
            chart_data = {
                'timestamps': last_100['timestamp'].dt.strftime('%Y-%m-%d %H:%M').tolist(),
                'prices': [float(x) if pd.notnull(x) else None for x in last_100['close'].tolist()],
                'rsi': [float(x) if pd.notnull(x) else None for x in last_100['RSI'].tolist()],
                'macd': [float(x) if pd.notnull(x) else None for x in last_100['MACD'].tolist()],
                'bollinger': {
                    'upper': [float(x) if pd.notnull(x) else None for x in last_100['BB_upper'].tolist()],
                    'middle': [float(x) if pd.notnull(x) else None for x in last_100['BB_middle'].tolist()],
                    'lower': [float(x) if pd.notnull(x) else None for x in last_100['BB_lower'].tolist()]
                }
            }
            print("Dados dos gráficos preparados com sucesso")
        except Exception as e:
            print(f"Erro ao preparar dados dos gráficos: {str(e)}")
            raise
        
        if analysis:
            return jsonify({
                'status': 'success',
                'symbol': symbol,
                'analysis': analysis,
                'chart_data': chart_data
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