import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Descargar datos de S&P500 Futures (ES)
data = yf.download("ES=F", start="2022-01-01", end="2025-01-01", interval="1d")

# Calcular medias móviles
data["MA20"] = data["Close"].rolling(20).mean()
data["MA50"] = data["Close"].rolling(50).mean()

# Graficar
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="ES Futures Close", linewidth=1.5)
plt.plot(data["MA20"], label="20-day MA", linestyle="--")
plt.plot(data["MA50"], label="50-day MA", linestyle="--")
plt.title("S&P500 Futures with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()
