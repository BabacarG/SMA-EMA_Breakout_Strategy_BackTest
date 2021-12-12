from binance.client import Client
import csv
import datetime
import pandas as pd
import mplfinance as mpf

api_key = 'WDpBVEVMc3wjLCAYQ4opBgpHNhDlT0ClZH25OZml4C0ocygkDR30JggMOr5kKYrK'
api_secret = '51iVBjoSMhu4NkU85d7SiVrGpMwOB2eyPTHbvKe1zW1iHWquhXqg3rIwcu29anKK'

client = Client(api_key, api_secret)

# prices = client.get_all_tickers()
#
# for price in prices:
#     print(prices)

# return string: Open time,Open,High,Low,Close,Volume,Close time,Quote asset volume,Number of trades,
# Taker buy base asset,Taker buy quote asset volume,Ignore.
# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_4HOUR)
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_4HOUR, "1 Sep, 2021")
csvfile = open('4hours.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')


for candlestick in candles:
    # print(candlestick)
    candlestick_writer.writerow(candlestick)
# print(len(candles))

# convert csv into dataframe to plot
pd4hours = pd.read_csv('4hours.csv', index_col=False, parse_dates=True, header=None)

# convert epoch time to DateTime
for i in range(len(pd4hours[0])):
    epoch = int(pd4hours.iloc[i][0]) / 1000
    date_time = datetime.datetime.fromtimestamp(epoch)
    # date_time = pd.to_datetime(epoch)
    pd4hours.at[i, 0] = date_time

# give column names
pd4hours.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                    'Number of trades', 'Taker buy base asset', 'Taker buy quote asset volume', 'Ignore']
print(pd4hours)

# drop useless columns
pd4hours.drop(columns=['Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset',
                       'Taker buy quote asset volume', 'Ignore'], inplace=True)

# put datetime as index
pd4hours.set_index('Date', inplace=True)

# creation and calculation for EMA
emaperiod = 60
multiplier = 2/(emaperiod+1)
pd4hours["EMA"] = ""
somme = 0
for i in range(0, emaperiod):
    somme += pd4hours.iloc[i][3]
SMA = somme / emaperiod
print(pd4hours)
pd4hours['EMA'] = pd4hours['EMA'].replace([1, 3], 999)
pd4hours.at[(emaperiod-1), 'EMA'] = SMA
# for i in range(emaperiod, len(pd4hours[0])):
#     pd4hours.at[i, 'EMA'] = pd4hours.at[i, 'Close'] * multiplier + pd4hours.at[i-1, 'EMA'] * (1 - multiplier)



# plot candlestick
print(pd4hours)
# mpf.plot(pd4hours, type='candle', style='binance')


csvfile.close()
