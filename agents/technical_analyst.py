from crewai import Agent
import pandas as pd
import ta  # Technical Analysis Library

class TechnicalAnalyzerAgent:
    def __init__(self):
        self.agent = Agent(
            role="Technical Market Analyst",
            goal="Analyze stock & forex market trends using technical indicators.",
            memory=True,
            backstory="An AI-powered chart analyst using RSI, MACD, and moving averages to identify trade opportunities.",
            verbose=True,
        )

    def analyze_technical_indicators(self, data: pd.DataFrame):
        """Compute RSI & MACD indicators for trend analysis"""
        data["rsi"] = ta.momentum.RSIIndicator(data["Close"], window=14).rsi()
        data["macd"] = ta.trend.MACD(data["Close"]).macd()

        latest_rsi = data["rsi"].iloc[-1]
        latest_macd = data["macd"].iloc[-1]

        signal = "Buy" if latest_rsi < 30 else "Sell" if latest_rsi > 70 else "Hold"

        return {
            "RSI": latest_rsi,
            "MACD": latest_macd,
            "Trading Signal": signal,
        }
