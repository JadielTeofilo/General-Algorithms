"""

 LRU Cache: Design and build a "least recently used " cache, which evicts the least recently used
item. The cache should map from keys to values (allowing you to insert and retrieve a value associ-
ated with a particular key) and be initialized with a max size. When it is full, it should evict the least recently used item.

Operations:

init 
in - max_size: int


insert
in - key: str, value: any
side-effect - remove lru if full


retrieve
in - key: str
out - value: any

keep a dict with reference to the Node data

Node will be part of a linked list that will work as a queue,
but items can be removed from the queue when referenced 

"""
import dataclasses
from typing import Optional, Dict, Any


@dataclasses.dataclass
class Node:
	key: str
	value: Any
	previous: Optional['Node'] = None
	next: Optional['Node'] = None

	def update_value(self, value: Any) -> None:
		self.value = value

@dataclasses.dataclass
class Queue:
	start: Optional['Node'] = None
	end: Optional['Node'] = None

	def insert(self, key: str, value: Any) -> Node:
		if not self.start or not self.end:
			self.start = Node(key, value)
			self.end = self.start
		else:
			self.end.next = Node(key, value, self.end)
			self.end = self.end.next
		return self.end

	def popleft(self) -> str:
		""" Removes the first element from queue and returns key """
		node_to_remove: Node = self.start
		next: Node = node_to_remove.next
		if not next:
			self.end = None
			self.start = None
		else:
			next.previous = None
			self.start = next
		return node_to_remove.key

	def remove(self, node: Node) -> None:
		previous: Optional['Node'] = node.previous
		next: Optional['Node'] = node.next
		# Update neighbors
		if previous:
			previous.next = next
		if next:
			next.previous = previous
		# Update Queue pointers if needed
		if self.start == node:
			self.start = self.start.next
		if self.end == node:
			self.end = self.end.previous

	def move_to_the_end(self, node: Node) -> Node:
		self.remove(node)
		self.insert(node.key, node.value)
		return self.end


class LruCache:
	
	def __init__(self, max_size: int) -> None:
		if not max_size:
			raise ValueError('Max size must be integer')
		self.queue: Queue = Queue()
		self.value_keys: Dict[str, Any] = {}
		self.max_size: int = max_size

	def insert(self, key: str, value: Any) -> None:
		if key in self.value_keys:
			self.value_keys[key].update_value(value)
			self.queue.move_to_the_end(self.value_keys[key])
			return
		self.value_keys[key] = self.queue.insert(key, value)
		if len(self.value_keys) > self.max_size:
			self.remove_lru()

	def remove_lru(self) -> None:
		key: str = self.queue.popleft()
		self.value_keys.pop(key)
			
	def retrieve(self, key: str) -> Any:
		if key not in self.value_keys:
			raise ValueError('Not a valid key')
		self.value_keys[key] = self.queue.move_to_the_end(self.value_keys[key])
		return self.value_keys[key].value


import pdb;pdb.set_trace()
