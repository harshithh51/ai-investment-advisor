from crewai import Agent
from langchain_core.tools import BaseTool
from tools import get_current_stock_price, search_tool

# Make sure tools are BaseTool-compatible
tools_list = [search_tool] if isinstance(search_tool, BaseTool) else []

data_explorer = Agent(
    role="Financial Data Researcher",
    goal="Get financial data for a stock",
    backstory="Expert at using Yahoo Finance and reading ratios.",
    verbose=True
)

news_info_explorer = Agent(
    role="News and Info Researcher",
    goal="Find the latest news about the company.",
    backstory="You're a powerful news scraper that knows the web deeply.",
    tools=tools_list,
    verbose=True
)

analyst = Agent(
    role="Data Analyst",
    goal="Combine financial and news data into useful insight.",
    backstory="You're a smart analyst who speaks in simple Indian finance language like Lakh and Crore.",
    verbose=True
)

fin_expert = Agent(
    role="Financial Expert",
    goal="Give the final investment decision: Buy, Hold, or Sell.",
    backstory="You're like Warren Buffet with better AI brains.",
    tools=[get_current_stock_price],
    verbose=True
)
