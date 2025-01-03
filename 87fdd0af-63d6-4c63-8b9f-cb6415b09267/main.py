from surmount.base_class import Strategy, TargetAllocation
from surmount.logging import log
import random

class TradingStrategy(Strategy):

   @property
   def assets(self):
      return ["MSFT", "AAPL", "UVXY"]

   @property
   def interval(self):
      return "1day"

   def run(self, data_functions):
     return TargetAllocation({"MSFT": 0.1, "AAPL": 0.4, "UVXY": 0.5 })