from bs4 import BeautifulSoup
import pandas as pd
import requests

def investing_com():
    url = "https://www.investing.com/equities/nvidia-corp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    divs = soup.select("dd[data-test='marketCap']")
    print(divs)
    
    divs_bs = BeautifulSoup(divs[0], "html.parser")
    spans = divs_bs.select("span")
    print(spans)
    
investing_com()

# Need to look at the data-test values in the html