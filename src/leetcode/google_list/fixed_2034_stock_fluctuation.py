"""
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

    Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
    Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
    Finds the maximum price the stock has been based on the current records.
    Finds the minimum price the stock has been based on the current records.

Implement the StockPrice class:

    StockPrice() Initializes the object with no price records.
    void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
    int current() Returns the latest price of the stock.
    int maximum() Returns the maximum price of the stock.
    int minimum() Returns the minimum price of the stock.

Another option is to keep it all sorted
sortedcontainers

SortedDict which allow us to have new keys be inserted in log n and keys always be sorted

in this case we would need the price to be sorted
rec: Dict[int, Set[int]]= sortedcontainrs.SortedDict()
time_to_price: Dict[int, int] = {}

1, 10
1, 20
1, 10






"""
import sortedcontainers
from typing import List, Tuple, Set, Dict


class StockPrice:

    def __init__(self):
        self.prices: Dict[int, Set[int]] = sortedcontainers.SortedDict()
        self.time_to_price: Dict[int, int] = {}
        self.curr: int | None = None

    def update(self, timestamp: int, price: int) -> None:
        self.curr = max(self.curr, timestamp)  if self.curr is not None else timestamp
        if self.time_to_price.get(timestamp) == price:
            return
        if price not in self.prices:
            self.prices[price] = set()
        if timestamp in self.time_to_price: 
            old_price: int = self.time_to_price[timestamp]
            self.prices[old_price].remove(timestamp)
            if not self.prices[old_price]:
                self.prices.pop(old_price)
        self.time_to_price[timestamp] = price
        self.prices[price].add(timestamp)

    def current(self) -> int:
        if self.curr is not None:
            return self.time_to_price[self.curr]

    def maximum(self) -> int:
        return self.prices.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.prices.peekitem(0)[0]



# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(1,10)
param_2 = obj.current()
param_3 = obj.maximum()
param_4 = obj.minimum()
