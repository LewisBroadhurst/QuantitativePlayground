import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
api_key = os.getenv('OANDA_API_KEY')
account_id = os.getenv('OANDA_ACCOUNT_ID')
oanda_url = os.getenv('OANDA_STREAM_URL')

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def stream_prices(pairs_list):
    
    print("Start price stream...")
    
    params = dict(
        instruments=','.join(pairs_list)
    )
    
    url = f"{oanda_url}/accounts/{account_id}/pricing/stream"
    
    response = requests.get(url, params=params, headers=headers, stream=True)
    
    for price in response.iter_lines():
        if price:
            decoded_price = json.loads(price.decode('utf-8'))
            print(decoded_price)
            print()