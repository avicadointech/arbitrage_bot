import requests
from binance.client import Client
import time

binance_api_key = ''
binance_api_secret = ''
client = Client(binance_api_key, binance_api_secret)

print('start')

status = 'botactive'
symbolsBinance = ['XRPUSDT', 'ATMUSDT', 'WAVESUSDT', 'DOTUSDT', 'PSGUSDT', 'ASRUSDT', 'ACMUSDT', 'AVAXUSDT', 'BATUSDT', 'LINKUSDT', 'OMGUSDT',
                  'DOTUSDT', 'THETAUSDT', 'BARUSDT', 'ALGOUSDT', 'BANDUSDT', 'ATOMUSDT', 'ENJUSDT', 'LTCUSDT',
                  'OXTUSDT', 'GRTUSDT', 'UNIUSDT']
symbolsParibu = ['XRP_TL', 'ATM_TL', 'WAVES_TL', 'DOT_TL', 'PSG_TL', 'ASR_TL', 'ACM_TL', 'AVAX_TL', 'BAT_TL', 'LINK_TL', 'OMG_TL', 'DOT_TL',
                 'THETA_TL', 'BAR_TL', 'ALGO_TL', 'BAND_TL', 'ATOM_TL', 'ENJ_TL', 'LTC_TL', 'OXT_TL', 'GRT_TL',
                 'UNI_TL']
lenSymbols = len(symbolsBinance)

while status == 'botactive':

    for i in range(lenSymbols):
        symbolParibu = symbolsParibu[i]
        response = requests.get("https://www.paribu.com/ticker")
        paribuFiatBid = response.json()[symbolParibu]['highestBid']
        paribuFiatAsk = response.json()[symbolParibu]['lowestAsk']

        symbolBinance = symbolsBinance[i]
        binanceData = client.get_ticker(symbol=symbolBinance)
        lastFiatCoin = binanceData['lastPrice']
        tryExchangeData = client.get_ticker(symbol='USDTTRY')
        tryExchange = tryExchangeData['lastPrice']
        lastFiatCoinTl = float(lastFiatCoin) * float(tryExchange)

        if paribuFiatBid > (lastFiatCoinTl + lastFiatCoinTl * 0.015):
            zaman = time.asctime()
            print(symbolBinance, 'Available Arbitrage. Price is higher in Paribu. Paribu Price(TRY):',
                  paribuFiatBid, 'Binance Price(USDT):', lastFiatCoin, 'Binance price(TRY):', lastFiatCoinTl, 'time:',
                  time)

        elif paribuFiatAsk < (lastFiatCoinTl - lastFiatCoinTl * 0.015):
            zaman = time.asctime()
            print(symbolBinance, 'Available Arbitrage. Price is higher in Binance. Paribu fiyatı(TRY):',
                  paribuFiatAsk, 'Binance price(USDT):', lastFiatCoin, 'Binance price(TRY):', lastFiatCoinTl, 'time:',
                  time)

        time.sleep(1)
