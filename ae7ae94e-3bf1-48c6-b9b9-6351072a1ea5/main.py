
from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI, EMA, SMA, MACD, MFI, BB
from surmount.logging import log

class TradingStrategy(Strategy):

   @property
   def assets(self):
      return ["NFLX"]

   @property
   def interval(self):
      return "1day"

   def run(self, data):
      data = data["ohlcv"]
      nflx_stake = 0
      nflx_bbands = BB("NFLX", data, 20, 1.4)

      if len(data)<20:
         return TargetAllocation({})

      current_price = data[-1]["NFLX"]['close']

      if nflx_bbands is not None:
         if current_price < nflx_bbands['lower'][-1] and current_price < nflx_bbands['lower'][-2] and current_price > nflx_bbands['lower'][-3] and current_price < nflx_bbands['upper'][-2] and current_price < nflx_bbands['upper'][-3]:
            nflx_stake = 0.5

      return TargetAllocation({"NFLX": nflx_stake})