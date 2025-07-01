import yfinance as yf
import time
from duckduckgo_search import DDGS
from langchain.tools import tool

@tool("Get current stock price")
def get_current_stock_price(symbol: str) -> str:
    try:
        time.sleep(0.5)
        stock = yf.Ticker(symbol)
        price = stock.info.get("regularMarketPrice") or stock.info.get("currentPrice")
        return f"{symbol} current price is ₹{price}" if price else "Price not available"
    except Exception as e:
        return f"Error: {e}"

@tool("Search news headlines")
def search_tool(query: str) -> str:
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            headlines = [r['title'] for r in results][:5]
            return "\n".join(headlines)
    except Exception as e:
        return f"Error fetching news: {e}"