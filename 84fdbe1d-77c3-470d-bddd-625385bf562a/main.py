from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.logging import log

class TradingStrategy(Strategy):

   def __init__(self):
      self.tickers = ["SWBI", "GM", "DE", "HD", "MCD"]
      self.weights = [0.2, 0.1 , 0.1 , 0.1, 0.1]
      self.equal_weighting = False
      self.count = 0

   @property
   def interval(self):
      return "1day"

   @property
   def assets(self):
      return self.tickers

   def run(self, data):
      self.count += 1
      if (self.count%30 == 1):
         if self.equal_weighting: 
            allocation_dict = {i: 1/len(self.tickers) for i in self.tickers}
         else:
            allocation_dict = {self.tickers[i]: self.weights[i] for i in range(len(self.tickers))} 
         return TargetAllocation(allocation_dict)
      return None