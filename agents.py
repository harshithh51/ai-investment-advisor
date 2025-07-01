from crewai import Agent
from tools import get_current_stock_price, search_tool

data_explorer = Agent(
    role="Financial Data Researcher",
    goal="Get financial data for a stock",
    backstory="You're skilled in Yahoo Finance and financial ratios.",
    verbose=True
)

news_info_explorer = Agent(
    role="News and Info Researcher",
    goal="Find the latest business news on a stock",
    tools=[search_tool],
    verbose=True
)

analyst = Agent(
    role="Data Analyst",
    goal="Combine financial data and news into an analysis",
    backstory="You use Indian units (Lakh/Crore) and simplify reports.",
    verbose=True
)

fin_expert = Agent(
    role="Financial Expert",
    goal="Give a Buy/Hold/Sell decision",
    tools=[get_current_stock_price],
    backstory="Think like Warren Buffet, explain decisions clearly.",
    verbose=True
)