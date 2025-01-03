
from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA, EMA
from surmount.logging import log

class TradingStrategy(Strategy):

   @property
   def assets(self):
      return ["QQQ"]

   @property
   def interval(self):
      return "1day"

   def run(self, data):
      data = data["ohlcv"]
      spy_stake = 0
      spy_sma = SMA("QQQ", data, 10)
      spy_ema = EMA("QQQ", data, 10)

      if spy_sma is not None and spy_ema is not None and len(spy_sma)>=2:
         if spy_sma[-1] > spy_ema[-1] and spy_sma[-2] < spy_ema[-2]:
            spy_stake = 0.5
         elif spy_sma[-1] < spy_ema[-1] and spy_sma[-2] > spy_ema[-2]:
            spy_stake = 0 

      return TargetAllocation({"QQQ": spy_stake})