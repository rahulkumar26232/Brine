from typing import Dict

import requests


def fetch_new_prices()-> Dict:
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page = 10 & page = 1 & sparkline = false"
    payload = {}
    response = requests.request("GET", url, data=payload)

    return response.json()