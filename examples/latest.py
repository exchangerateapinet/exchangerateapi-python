import os
from exchangerateapi.client import ExchangeRateApiClient

api_key = os.getenv("EXCHANGERATEAPI_KEY", "YOUR_API_KEY")
client = ExchangeRateApiClient(api_key=api_key)

# Scenario 1: latest with base only
latest_usd = client.latest(base="USD")
print("Latest USD sample codes:", list(latest_usd.get("rates", {}).keys())[:5])

# Scenario 2: latest with symbols filter
latest_eur_subset = client.latest(base="EUR", symbols=["USD", "GBP", "JPY"])
print("Latest EUR subset:", {k: latest_eur_subset.get("rates", {}).get(k) for k in ["USD", "GBP", "JPY"]})
