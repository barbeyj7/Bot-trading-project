#!/usr/bin/env python3
# -*- coding: utf-8 -*-


pip install python-binance
pip install ta
import pandas as pd
from binance.client import Client
import ta

klinesT = Client().get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "01 January 2017")
df = pd.DataFrame(klinesT, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])

     


print(df)

#Cleaning 

del df['ignore']
del df['close_time']
del df['quote_av']
del df['trades']
del df['tb_base_av']
del df['tb_quote_av']

df['close'] = pd.to_numeric(df['close'])
df['high'] = pd.to_numeric(df['high'])
df['low'] = pd.to_numeric(df['low'])
df['open'] = pd.to_numeric(df['open'])
print(df)

df = df.set_index(df['timestamp'])
df.index = pd.to_datetime(df.index, unit='ms')

del df['timestamp']
print(df)
     
                         open      high       low     close         volume
timestamp                                                                 
2017-08-17 04:00:00   4261.48   4313.62   4261.32   4308.83    47.18100900
2017-08-17 05:00:00   4308.83   4328.69   4291.37   4315.32    23.23491600
2017-08-17 06:00:00   4330.29   4345.45   4309.37   4324.35     7.22969100
2017-08-17 07:00:00   4316.62   4349.99   4287.41   4349.99     4.44324900
2017-08-17 08:00:00   4333.32   4377.85   4333.32   4360.69     0.97280700
...                       ...       ...       ...       ...            ...
2021-08-03 04:00:00  38658.48  38828.59  38211.00  38328.01  3262.56820200
2021-08-03 05:00:00  38328.01  38378.25  37955.52  38254.85  3774.60379900
2021-08-03 06:00:00  38254.85  38449.97  38199.69  38357.16  1387.67780100
2021-08-03 07:00:00  38357.16  38665.75  38252.40  38593.44  2015.56702900
2021-08-03 08:00:00  38593.43  38666.00  38315.00  38530.14  1322.38610600

[34613 rows x 5 columns]

df['SMA200'] = ta.trend.sma_indicator(df['close'], 200)
df['SMA600'] = ta.trend.sma_indicator(df['close'], 600)
print(df)
     
                         open      high  ...       SMA200        SMA600
timestamp                                ...                           
2017-08-17 04:00:00   4261.48   4313.62  ...          NaN           NaN
2017-08-17 05:00:00   4308.83   4328.69  ...          NaN           NaN
2017-08-17 06:00:00   4330.29   4345.45  ...          NaN           NaN
2017-08-17 07:00:00   4316.62   4349.99  ...          NaN           NaN
2017-08-17 08:00:00   4333.32   4377.85  ...          NaN           NaN
...                       ...       ...  ...          ...           ...
2021-08-03 04:00:00  38658.48  38828.59  ...  39654.68730  34845.906650
2021-08-03 05:00:00  38328.01  38378.25  ...  39673.20655  34854.671100
2021-08-03 06:00:00  38254.85  38449.97  ...  39691.70845  34863.818533
2021-08-03 07:00:00  38357.16  38665.75  ...  39707.77055  34873.290583
2021-08-03 08:00:00  38593.43  38666.00  ...  39716.58390  34882.827200

usdt = 1000
btc = 0
lastIndex = df.first_valid_index()

for index, row in df.iterrows():
  if df['SMA200'][lastIndex] > df['SMA600'][lastIndex] and usdt > 10:
    btc = usdt / df['close'][index] 
    btc = btc - 0.0007 * btc
    usdt = 0
    print("Buy BTC at",df['close'][index],'$ the', index)

  if df['SMA200'][lastIndex] < df['SMA600'][lastIndex] and btc > 0.0001:
    usdt = btc * df['close'][index]
    usdt = usdt - 0.0007 * usdt
    btc = 0
    print("Sell BTC at",df['close'][index],'$ the', index)
  lastIndex = index
     

finalResult = usdt + btc * df['close'].iloc[-1]
print("Final result",finalResult,'USDT')
     
Final result 17325.62319936932 USDT

     
