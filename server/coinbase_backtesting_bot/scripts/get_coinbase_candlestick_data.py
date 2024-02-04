import os
import datetime as dt
import sys
sys.path.append("../../")

from coinbase.rest import RESTClient
from json import dumps
from dotenv import dotenv_values, load_dotenv

from coinbase_backtesting_bot.scripts.helpers import convert_coinbase_granularity_into_time

load_dotenv()
secrets = dotenv_values(".env")

api_key = os.getenv('COINBASE_API_KEY_TRADING_040224')
api_secret = os.getenv('COINBASE_API_SECRET_TRADING_040224')
client = RESTClient(api_key=api_key, api_secret=api_secret)
filename_prefix = "COINBASE_CANDLESTICKS_"

## Script to get Cryptocurrency Candles from Coinbase.
## Max 300 at once.
if __name__ == "__main__":
    sys.path.insert(0, 'E:\workspace\CoinbaseTradingviewFinanceFun\server')
    print(sys.path)
    
    ## Converter for UNIX into standard time useful for better file names
    ## Convert response into .pkl file
    ## If number of candles > 300 split into multiple requests, then join data together.
    
    # 1. Enter time dates the script should retrive from and to
    # e.g. dt.datetime(2023, 1, 1, 14, 30).timestamp()
    datetime_from = dt.datetime(2023, 1, 1)
    datetime_to = dt.datetime(2024, 1, 1)
    
    # 2. Enter Granularity [ONE_MINUTE... FIFTEEN_MINUTE... ONE_DAY...] and Product [BTC-USD, ETH-USD...]
    granularity = "ONE_DAY"
    product = "BTC-USD"
    
    # Script
    if datetime_from >= datetime_to:
        sys.exit("datetime_from must be less than datetime_to")
        
    time_range = datetime_to - datetime_from
    # granularity_in_posix = convert_coinbase_granularity_into_time(granularity)
    # number_of_candlesticks = time_range / granularity_in_posix
    # print(number_of_candlesticks)
        
    # candles_response = client.get_candles(product, datetime_from.timestamp(), datetime_to.timestamp(), granularity)
    # candles_list = candles_response['candles']
    