"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

    Logger() Initializes the logger object.
    bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


We need to keep somewhat of a set of the last 10 seconds

In - time: int, message: str

if we keep a queue we can remove the first invalid elements at each step of the way
we keep also a set to have the messages checked
O(n) time n being the size of the queue O(n) space n size of queue


Another approach is to keep a hash with all messages and their last occurence, we update only the curr message each time O(1) time complexity  O(m) space where m is all the messages sent
 

"""
import collections
from typing import Dict, Set


TimeLog = collections.namedtuple('TimeLog', 'msg timestamp')


class Logger:

    def __init__(self):
        self.unique_messages: Set[str] = set()
        self.ordered_messages: Deque[TimeLog] = collections.deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while (self.ordered_messages and 
               self.ordered_messages[0].timestamp + 10 <= timestamp):
            popped_message: str = self.ordered_messages.popleft().msg
            self.unique_messages.discard(popped_message)
        if message in self.unique_messages:
            return False
        self.unique_messages.add(message)
        self.ordered_messages.append(TimeLog(message, timestamp))
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
