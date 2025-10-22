import os
from exchangerateapi.client import ExchangeRateApiClient

api_key = os.getenv("EXCHANGERATEAPI_KEY", "YOUR_API_KEY")
client = ExchangeRateApiClient(api_key=api_key)

# Scenario 1: historical for a date with base only
hist_usd = client.historical(date="2024-01-02", base="USD")
print("Historical USD sample codes:", list(hist_usd.get("rates", {}).keys())[:5])

# Scenario 2: historical for a date with symbols filter
hist_eur_subset = client.historical(date="2024-01-02", base="EUR", symbols=["USD", "GBP", "JPY"])
print("Historical EUR subset:", {k: hist_eur_subset.get("rates", {}).get(k) for k in ["USD", "GBP", "JPY"]})
