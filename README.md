# USstock

A Streamlit-based web application for analyzing stocks using real-time data from Yahoo Finance and AI-powered insights from the Perplexity API.

## Features

- Real-time stock data visualization using candlestick charts
- Key financial metrics display (Current Price, Market Cap, P/E Ratio)
- AI-powered stock analysis and news insights
- Custom query capability for specific stock-related questions
- User-friendly interface with customizable time periods

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YBridge/USstock.git
   cd USstock
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your Perplexity API key:
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Enter a stock symbol and select a time period to analyze

4. Use the custom query feature to ask specific questions about the stock

## Requirements

- Python 3.8+
- Streamlit
- yfinance
- plotly
- python-dotenv
- Perplexity API key

## License

MIT License
