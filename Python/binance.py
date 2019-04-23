from binance.client import Client
client = Client(api_key, api_secret)

# ===== client.cancel_order( ** params ) =====
# Отменить активный заказ. Должен быть отправлен либо orderId, либо origClientOrderId.
# symbol(str) - требуется
# orderId(int) - уникальный идентификатор заказа
# recvWindow(int) - количество миллисекунд, которое запрос действителен для
# Возвращает:
{"symbol": "LTCBTC",
 "origClientOrderId": "myOrder1",
 "orderId": 1,
 "clientOrderId": "cancelMyOrder1"
 }

# ===== client.get_account( ** params )
# Получите информацию о текущем счете.
#
# Параметры: recvWindow(int) - количество миллисекунд, которое запрос действителен для
# Возвращает:
{
    "makerCommission": 15,
    "takerCommission": 15,
    "buyerCommission": 0,
    "sellerCommission": 0,
    "canTrade": true,
    "canWithdraw": true,
    "canDeposit": true,
    "balances": [
        {
            "asset": "BTC",
            "free": "4723846.89208129",
            "locked": "0.00000000"
        },
        {
            "asset": "LTC",
            "free": "4763368.68006011",
            "locked": "0.00000000"
        }
    ]
}
поднимает: BinanceRequestException, BinanceAPIException

# ===== client.get_historical_klines(symbol, interval, start_str, end_str=None)
# Get Historical Klines from Binance
# If using offset strings for dates add “UTC” to date string e.g. “now UTC”,
# “11 hours ago UTC”

# Parameters:
# symbol(str) – Name of symbol pair e.g BNBBTC
# interval(str) – Binance Kline interval
# start_str(str | int) – Start date string in UTC format or timestamp in milliseconds
# end_str(str | int) – optional - end date string in UTC format or timestamp in milliseconds(default will fetch everything up to now)
# Returns:
# list of OHLCV values

KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_1MONTH = '1M'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'

        1499040000000,      # Open time
        "0.01634790",       # Open
        "0.80000000",       # High
        "0.01575800",       # Low
        "0.01577100",       # Close
        "148976.11427815",  # Volume
        1499644799999,      # Close time
        "2434.19055334",    # Quote asset volume
        308,                # Number of trades
        "1756.87402397",    # Taker buy base asset volume
        "28.46694368",      # Taker buy quote asset volume
        "17928899.62484339" # Can be ignored