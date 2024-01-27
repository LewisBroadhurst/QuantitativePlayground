import os
from data_providers.oanda_api import OandaApi
from pricing_streams.oanda.oanda_stream_prices import stream_prices
### The file where this is run from, is the point at which everything else should reference
### This is why there are issues when trying to run the application from specific folders. 
### The main (or 'main' equivalent) should be in the root directory            
if __name__ == '__stream_prices__':
    api = OandaApi()
    stream_prices(['EUR_USD'])
    print("End...")
    