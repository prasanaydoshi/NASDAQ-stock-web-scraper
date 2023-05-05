import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import string
import csv
from csv import DictWriter
import requests
import os


from urllib.request import Request, urlopen

letters = string.ascii_uppercase
letters += "0"
finalList = []

for letter in letters:
    req = Request(
        url='https://www.advfn.com/nasdaq/nasdaq.asp?companies=' + letter,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    tables = pd.read_html(urlopen(req).read())
    df = tables[4]
    firstColumn = df.iloc[:, [1]]
    firstList = firstColumn.values.tolist()
    del firstList[:2]
    for sublist in firstList:
        for element in sublist:
            finalList.append(element)

#print(finalList)
#AMZN?p=AMZN
#AMZN/key-statistics?p=AMZN
#AMZN/history?period1=863654400&period2=1682985600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
#/financials?p=
#/balance-sheet?p=
start_url = "https://finance.yahoo.com/quote/"
#url_endings = ["?p=","/key-statistics?p=", "/financials?p=", "/balance-sheet?p=", "/cash-flow?p="]
#historical_data_url = "history?period1=863654400&period2=1682985600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
url_list = []

for stocks in finalList:
    #for url in url_endings:
    url_list.append(start_url+stocks+"?p="+stocks)

test_list = url_list[:200]
#print(test_list)
previous_close = []
open_ = []
bid =[]
ask = []
day_range = []
week_range = []
volume = []
avg_volume =[]
market_cap = []
beta = []
pe_ratio = []
eps = []
earnings_date = []
dividend_yield = []
exDividend_date = []
year_target_est = []
stock_list = []

def stats(url):
    df = pd.read_html(url)
    cs = df[1]
    firstColumns = cs.iloc[:, [0, 1]]
    market_cap.append(cs.iloc[0,1])
    beta.append(cs.iloc[1,1])
    pe_ratio.append(cs.iloc[2,1])
    eps.append(cs.iloc[3,1])
    earnings_date.append(cs.iloc[4,1])
    dividend_yield.append(cs.iloc[5,1])
    exDividend_date.append(cs.iloc[6,1])
    year_target_est.append(cs.iloc[7,1])

def vals(url):
    df = pd.read_html(url)
    cs = df[0]
    firstColumns = cs.iloc[:, [0, 1]]
    previous_close.append(cs.iloc[0,1])
    open_.append(cs.iloc[1,1])
    bid.append(cs.iloc[2,1])
    ask.append(cs.iloc[3,1])
    day_range.append(cs.iloc[4,1])
    week_range.append(cs.iloc[5,1])
    volume.append(cs.iloc[6,1])
    avg_volume.append(cs.iloc[7,1])

tmp = "https://finance.yahoo.com/quote/AMZN?p=AMZN"
def summary(url):
        stats(url)
        vals(url)

previous_close.append('Previous Close')
open_.append('Open')
bid.append('Bid')
ask.append('Ask')
day_range.append('Days Range')
week_range.append('52 Week Range')
volume.append('Volume')
avg_volume.append('Avg. Volume')
market_cap.append('Market Cap')
beta.append('Beta (5Y Monthly)')
pe_ratio.append('PE Ratio (TTM)')
eps.append('EPS (TTM)')
earnings_date.append('Earnings Date')
dividend_yield.append('Forward Dividend & Yield')
exDividend_date.append('Forward Dividend & Yield')
year_target_est.append('1y Target Est')
for i in range(len(test_list)):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    r = requests.get(test_list[i])
    if r.status_code == 200:
        summary(test_list[i])
        stock_list.append(finalList[i])
#tmp_list = market_cap[:30]
#print(tmp_list)

def make_csv():
    stock_list.insert(0, ' ')
    print_list = [stock_list, previous_close, open_, bid, ask, day_range, week_range, volume, avg_volume, market_cap, beta, pe_ratio, eps, earnings_date, dividend_yield,
                  exDividend_date, year_target_est]
    my_df = pd.DataFrame(print_list)
    my_df.to_csv('stock_data.csv', index=False, header=False)
    #with open('stock_data.csv', 'w', newline="") as f:
    #finalList.insert(0, " ")
    #writer = csv.DictWriter(f, fieldnames=finalList)
    #writer.writeheader()
    #writer.writerows(new_list)
make_csv()