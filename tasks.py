from crewai import Task
from agents import data_explorer, news_info_explorer, analyst, fin_expert

get_company_financials = Task(
    description="Get income statements and key financial info for {stock}",
    agent=data_explorer
)

get_company_news = Task(
    description="Get the latest business news for {stock}",
    agent=news_info_explorer
)

analyse = Task(
    description="Do a detailed financial analysis for {stock}",
    agent=analyst,
    context=[get_company_financials, get_company_news]
)

advise = Task(
    description="Give a final investment decision: Buy, Hold, or Sell for {stock}",
    agent=fin_expert,
    context=[analyse],
    output_file="Recommendation.md"
)