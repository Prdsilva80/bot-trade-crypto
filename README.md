# Bot de Trading de Criptomoedas / Cryptocurrency Trading Bot

[English Version](#english-version)

## Português

### Descrição
Bot de trading de criptomoedas que utiliza análise técnica e machine learning para monitorar e analisar o mercado de criptomoedas em tempo real. O sistema integra-se com a API da Binance e fornece uma interface web interativa para visualização de dados e análises.

### Funcionalidades
- Integração com API pública da Binance
- Análise técnica com múltiplos indicadores:
  - RSI (Índice de Força Relativa)
  - MACD (Moving Average Convergence Divergence)
  - Bandas de Bollinger
- Machine Learning para análise de mercado
- Dashboard interativo com gráficos em tempo real
- Suporte a múltiplos pares de trading (BTC, ETH, BNB, etc.)
- Atualização automática de preços e indicadores

### Tecnologias Utilizadas
- Python 3.8+
- Flask (Framework Web)
- pandas (Análise de Dados)
- scikit-learn (Machine Learning)
- python-binance (API Binance)
- Chart.js (Visualização de Dados)
- Bootstrap 5 (Interface)

### Requisitos
```
python-binance
flask
pandas
numpy
scikit-learn
python-dotenv
```

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Prdsilva80/bot-trade-crypto.git
cd bot-trade-crypto
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto:
```
BINANCE_API_KEY=sua_api_key_aqui
BINANCE_API_SECRET=sua_api_secret_aqui
```

### Executando o Projeto
1. Ative o ambiente virtual
2. Execute o servidor Flask:
```bash
python app.py
```
3. Acesse `http://127.0.0.1:5000` no navegador

---

## English Version

### Description
Cryptocurrency trading bot that uses technical analysis and machine learning to monitor and analyze the cryptocurrency market in real-time. The system integrates with the Binance API and provides an interactive web interface for data visualization and analysis.

### Features
- Binance public API integration
- Technical analysis with multiple indicators:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands
- Machine Learning for market analysis
- Interactive dashboard with real-time charts
- Support for multiple trading pairs (BTC, ETH, BNB, etc.)
- Automatic price and indicator updates

### Technologies Used
- Python 3.8+
- Flask (Web Framework)
- pandas (Data Analysis)
- scikit-learn (Machine Learning)
- python-binance (Binance API)
- Chart.js (Data Visualization)
- Bootstrap 5 (Interface)

### Requirements
```
python-binance
flask
pandas
numpy
scikit-learn
python-dotenv
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Prdsilva80/bot-trade-crypto.git
cd bot-trade-crypto
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the project root:
```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

### Running the Project
1. Activate the virtual environment
2. Run the Flask server:
```bash
python app.py
```
3. Access `http://127.0.0.1:5000` in your browser


### Important Notes
- This is a demonstration project
- The bot uses the Binance public API for data collection
- No real trades are executed
- For educational purposes only