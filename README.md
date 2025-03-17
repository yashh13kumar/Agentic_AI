
 Agentic AI - Financial Assistant

 Overview
Agentic AI is a financial assistant that leverages local AI models (LLaMA 3) and real-time data sources to provide stock market insights, fundamental analysis, and financial news summaries. The system integrates:
- Ollama for LLM-based responses.
- Yahoo Finance (yfinance) for stock data retrieval.
- DuckDuckGo Search (DDGS) for fetching the latest financial news.

 Features
- Fetches stock information such as price, market cap, and P/E ratio.
- Retrieves the latest news related to the stock from the web.
- Generates a summarized financial report using LLaMA 3.

 Installation
 Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Ollama (for running local LLM models)
- Required Python libraries:
  ```bash
  pip install ollama yfinance duckduckgo_search
  ```

 Running the Project
1. Start Ollama (Ensure LLaMA 3 is installed)
   ```bash
   ollama run llama3
   ```
2. Run the script
   ```bash
   python financial_agent.py
   ```

 Example Output
```
Stock Summary for AAPL:
- Name: Apple Inc.
- Price: $213.49
- Market Cap: $3,207 billion
- P/E Ratio: 33.89

Latest News:
1. Yahoo Finance's latest news and headlines for AAPL
2. A news article on why AAPL shares are getting obliterated today
3. Google Finance's stock price and news page for AAPL

Summary:
[LLM Generated Summary]
```

 Future Improvements
- Enhance news search by integrating multiple sources.
- Expand to include more financial indicators (e.g., dividends, earnings reports).
- Add interactive chatbot support for financial queries.

 Contributing
Feel free to contribute by submitting pull requests or reporting issues!



