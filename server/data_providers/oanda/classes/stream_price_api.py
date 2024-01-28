from data_providers.oanda.classes.base_price_api import OandaApiPrice

class StreamApiPrice(OandaApiPrice):
    
    def __init__(self, api_object):
        super().__init__(api_object)
        
    def __repr__(self):
        return f"StreamApiPrice {self.ask} {self.bid}"    