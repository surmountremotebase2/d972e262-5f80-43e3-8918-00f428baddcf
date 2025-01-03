
from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA, BB
from surmount.logging import log

class TradingStrategy(Strategy):

   @property
   def assets(self):
      return ["SPY", "AAPL"]

   @property
   def interval(self):
      return "1day"

   def run(self, data):
      data = data["ohlcv"]
      spy_stake = 0
      aapl_stake = 0

      spy_sma = SMA("SPY", data, 10)

      if len(data)<10:
         return TargetAllocation({})

      current_price = data[-1]["SPY"]['close']

      if spy_sma is not None and len(spy_sma)>=2:
         if (current_price - spy_sma[-2])/spy_sma[-2] < -0.05:
            spy_stake = 0
            aapl_stake = 0.5
         elif (current_price - spy_sma[-2])/spy_sma[-2] > 0.05:
            spy_stake = 0.5
            aapl_stake = 0

      return TargetAllocation({"SPY": spy_stake, "AAPL": aapl_stake})