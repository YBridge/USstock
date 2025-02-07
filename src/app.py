import os
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
from dotenv import load_dotenv
from services.perplexity_api import PerplexityAPI

# Load environment variables
load_dotenv()

# Initialize Perplexity API
perplexity_api = PerplexityAPI(api_key=os.getenv('PERPLEXITY_API_KEY'))

def load_stock_data(symbol, period='1y'):
    """Load stock data using yfinance"""
    stock = yf.Ticker(symbol)
    hist = stock.history(period=period)
    return hist, stock.info

def plot_stock_data(data, title):
    """Create stock price plot using plotly"""
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                        open=data['Open'],
                                        high=data['High'],
                                        low=data['Low'],
                                        close=data['Close'])])
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price')
    return fig

def main():
    st.set_page_config(page_title='Stock Analysis App', layout='wide')
    st.title('Stock Analysis App')

    # Sidebar
    st.sidebar.header('Settings')
    symbol = st.sidebar.text_input('Enter Stock Symbol:', value='AAPL').upper()
    period = st.sidebar.selectbox('Select Time Period:', 
                                ['1mo', '3mo', '6mo', '1y', '2y', '5y', 'max'],
                                index=3)

    if symbol:
        try:
            # Load stock data
            data, info = load_stock_data(symbol, period)
            
            # Display basic info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric('Current Price', f"${info.get('currentPrice', 'N/A'):.2f}")
            with col2:
                st.metric('Market Cap', f"${info.get('marketCap', 0)/1e9:.2f}B")
            with col3:
                st.metric('P/E Ratio', f"{info.get('trailingPE', 'N/A'):.2f}")

            # Plot stock data
            st.plotly_chart(plot_stock_data(data, f'{symbol} Stock Price'), use_container_width=True)

            # News and Analysis
            st.header('News and Analysis')
            
            # Custom Query
            query = st.text_input('Ask a question about the stock:', 
                                placeholder='e.g., What are the key factors affecting the stock price?')
            
            if query:
                with st.spinner('Analyzing...'):
                    response = perplexity_api.custom_query(f"{query} for {symbol} stock")
                    st.write(response)

            # Recent News
            with st.spinner('Fetching recent news...'):
                news = perplexity_api.custom_query(
                    f"What are the most recent significant news and developments for {symbol} stock? "
                    f"Provide a brief analysis of their potential impact on the stock price."
                )
                st.write(news)

        except Exception as e:
            st.error(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
