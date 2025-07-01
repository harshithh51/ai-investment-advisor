import streamlit as st
from crewai import Crew, Process
from agents import data_explorer, news_info_explorer, analyst, fin_expert
from tasks import get_company_financials, get_company_news, analyse, advise

st.set_page_config(page_title="AI Investment Advisor", layout="centered")
st.title("📈 AI-Powered Investment Advisor")
st.markdown("Enter a stock symbol (e.g., AAPL, TSLA, RELIANCE.NS) and get a full investment report.")

stock = st.text_input("Enter Stock Symbol:", value="AAPL")
run_analysis = st.button("Run Analysis")

if run_analysis and stock:
    with st.spinner("Running AI analysis..."):
        crew = Crew(
            agents=[data_explorer, news_info_explorer, analyst, fin_expert],
            tasks=[get_company_financials, get_company_news, analyse, advise],
            verbose=True,
            process=Process.sequential
        )
        result = crew.kickoff(inputs={'stock': stock})
        st.success("✅ Done!")
        st.markdown("### 💼 Final Recommendation")
        st.markdown(result)
        st.markdown("### 📄 Full Report")
        try:
            with open("Recommendation.md", "r") as f:
                st.markdown(f.read())
        except:
            st.warning("No report file found.")
else:
    st.info("Enter a stock symbol and click Run Analysis to start.")