import os
import datetime as dt
import sys
sys.path.append("../../")

from coinbase.rest import RESTClient
from json import dumps
from dotenv import dotenv_values, load_dotenv
from math import ceil

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
    
    # exit early if incorrect datetimes
    if datetime_from >= datetime_to:
        sys.exit("datetime_from must be less than datetime_to")
        
    time_range = datetime_to - datetime_from
    granularity_in_posix = convert_coinbase_granularity_into_time(granularity)
    number_of_candlesticks = int(time_range.total_seconds() / granularity_in_posix)
    number_of_requests_required = ceil(number_of_candlesticks / 300)
    
    print(f"Getting the candlestick data for {product} from {datetime_from} to {datetime_to}.")
    print(f"This will require {number_of_requests_required} requests to get {number_of_candlesticks} candlesticks.")
    
    if number_of_requests_required == 1:
        candles_response = client.get_candles(product, datetime_from.timestamp(), datetime_to.timestamp(), granularity)
        candles_list = candles_response['candles']
        
        # Check if .pkl file exists with same name
        # If yes look to add _1, _2, _3 in a while loop until its a new file name
    else:
        length_of_time_for_segment = time_range / number_of_requests_required
        current_segment_end = datetime_from + length_of_time_for_segment
        candlestick_data_segments = []
        
        for i in range(1, number_of_requests_required):
            candles_response = client.get_candles(product, datetime_from.timestamp(), datetime_to.timestamp(), granularity)
            candles_list = candles_response['candles']
        
        
        
        
    
    