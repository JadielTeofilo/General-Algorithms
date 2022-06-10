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


history: Dict[int, int]

1, 10
2, 12
1, 20
1, 10

on every update, if already present, add to stales and to the heaps

when looking at min and max, discard the stales

min_prices: List[HistoryEntry]
max_prices: List[Tuple[int, HistoryEntry]]

stales: Set[HistoryEntry]


O(log n) update
O(log n) max/min 
------------------------

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
import collections
import heapq
from typing import List, Tuple, Set, Dict


HistoryEntry = collections.namedtuple('HistoryEntry', 'price timestamp')


class StockPrice:

    def __init__(self):
        self.history: Dict[int, int] = {}
        self.min_prices: List[HistoryEntry] = []
        self.max_prices: List[Tuple[int, HistoryEntry]] = []
        self.stales_min: Dict[HistoryEntry, int] = collections.defaultdict(int)
        self.stales_max: Dict[HistoryEntry, int] = collections.defaultdict(int)
        self.curr: int | None = None

    def update(self, timestamp: int, price: int) -> None:
        entry: HistoryEntry = HistoryEntry(price, timestamp)
        self.curr = max(self.curr, timestamp)  if self.curr is not None else timestamp
        if self.history.get(timestamp) == price:
            return
        heapq.heappush(self.min_prices, entry)
        heapq.heappush(self.max_prices, (-price, entry))
        if timestamp not in self.history: 
            self.history[timestamp] = price
            return
        self.stales_max[(self.history[timestamp], timestamp)] += 1  
        self.stales_min[(self.history[timestamp], timestamp)] += 1 
        self.history[timestamp] = price

    def current(self) -> int:
        if self.curr is not None:
            return self.history[self.curr]

    def maximum(self) -> int:
        while self.stales_max[self.max_prices[0][1]] > 0:
            _, entry = heapq.heappop(self.max_prices)
            self.stales_max[entry] -= 1
        return self.max_prices[0][1].price

    def minimum(self) -> int:
        while self.stales_min[self.min_prices[0]] > 0:
            entry: HistoryEntry = heapq.heappop(self.min_prices)
            self.stales_min[entry] -= 1
        return self.min_prices[0].price           



# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(1,10)
param_2 = obj.current()
param_3 = obj.maximum()
param_4 = obj.minimum()
