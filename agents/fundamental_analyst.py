from crewai import Agent
import requests
import openai

class FundamentalAnalyzerAgent:
    def __init__(self, openai_api_key):
        self.agent = Agent(
            role="Fundamental Analyst",
            goal="Analyze financial news and macroeconomic trends for trading insights.",
            memory=True,
            backstory="A financial expert analyzing economic news, interest rates, and company earnings to predict market movements.",
            verbose=True,
        )
        self.openai_api_key = openai_api_key

    def fetch_news_sentiment(self, query="forex market"):
        """Fetch news headlines and analyze sentiment using LLM"""
        response = requests.get(f"https://newsapi.org/v2/everything?q={query}&apiKey=YOUR_NEWSAPI_KEY")
        articles = response.json().get("articles", [])

        summaries = [article["title"] + ": " + article["description"] for article in articles[:5]]

        analysis_prompt = f"Analyze the following financial news and provide sentiment analysis (positive, neutral, or negative):\n\n{summaries}"
        sentiment_analysis = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": analysis_prompt}]
        )

        return sentiment_analysis["choices"][0]["message"]["content"]
