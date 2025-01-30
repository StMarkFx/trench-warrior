from crewai import Agent
import yfinance as yf

class MarketObserverAgent:
    def __init__(self):
        self.agent = Agent(
            role="Market Data Observer",
            goal="Fetch real-time stock and forex market data.",
            memory=True,
            backstory=(
                "An AI market analyst who gathers real-time price movements, "
                "trading volumes, and historical trends for analysis."
            ),
            verbose=True,
        )

    def fetch_market_data(self, symbol="EURUSD=X"):
        """Fetch market data from Yahoo Finance"""
        data = yf.download(symbol, period="1d", interval="1h")
        return data.tail(1)  # Return the latest market data
