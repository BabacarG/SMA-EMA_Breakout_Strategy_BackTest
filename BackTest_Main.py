from CryptoBackTest import *

# Paste your own api keys which you can get by creating a Binance account
api_key = 'WDpBVEVMc3wjLCAYQ4opBgpHNhDlT0ClZH25OZml4C0ocygkDR30JggMOr5kKYrK'
api_secret_key = '51iVBjoSMhu4NkU85d7SiVrGpMwOB2eyPTHbvKe1zW1iHWquhXqg3rIwcu29anKK'

# Enter a ticker symbol (ex: ETHUSDT, ETHBTC, SOLUSDT...)
asset = "BTCUSDT"

# Available timeframes : 1min, 3min, 5min, 15min, 30min, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1m
timeFrame = "1d"

# Choose a start date for the data (Follow this format: "1 Jan, 2020")
startDate = "1 Jan, 2015"

backtest1 = CryptoBackTest(api_key, api_secret_key, asset, timeFrame, startDate)

# You can display the raw data graph but a graph will be opened in anyway after a backtest
# backtest1.plot()

# Choose if you want to use SMA or EMA and enter as parameter the range of SMA/EMA periods you want to compare
backtest1.buysell1sma(2, 10)
# backtest1.buysell1ema(2, 10)
