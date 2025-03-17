import ollama
import yfinance as yf
from duckduckgo_search import DDGS

def query_ollama(prompt, model="llama3"):
    """Query Ollama's local LLM"""
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

def get_stock_info(ticker):
    """Fetch stock price & fundamentals"""
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "Name": info.get("longName", "N/A"),
        "Symbol": ticker,
        "Price": info.get("currentPrice", "N/A"),
        "Market Cap": info.get("marketCap", "N/A"),
        "P/E Ratio": info.get("trailingPE", "N/A"),
    }

def get_latest_news(query):
    """Fetch latest news using DuckDuckGo search"""
    try:
        with DDGS() as search:
            results = list(search.text(query, max_results=3))
            return results
    except Exception as e:
        return [f"Error: {str(e)}"]

# Example Usage
ticker = "AAPL"
stock_data = get_stock_info(ticker)
news_data = get_latest_news(f"{ticker} stock news")

# Format results
prompt = f"""
Stock Summary for {ticker}:
- Name: {stock_data['Name']}
- Price: ${stock_data['Price']}
- Market Cap: {stock_data['Market Cap']}
- P/E Ratio: {stock_data['P/E Ratio']}

Latest News:
"""

for i, news in enumerate(news_data):
    if isinstance(news, dict) and "title" in news and "href" in news:
        prompt += f"{i+1}. {news['title']} - {news['href']}\n"

prompt += "\nSummarize this information."

response = query_ollama(prompt)
print(response)
