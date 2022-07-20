"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.




we need to keep track of the usage of items


[1 2 3 1 4]


1: 2
2: 1
3: 1

then we would remove the 2


we could have the inverted hash

2: [1]
1: [2, 3]  # its important that the keys inside be sorted by usage

and also the store hash
1: value, usage
2: value, usage
3: value, usage

get 
    looks up the store (value and usage)
    updates the usage_store (OrderedDict inside)
        removes from usage -1 and put on usage

insert
    lookups up the store
    in case of insert
        evicts if needed
            get the first key from the usage_store (OrderedDict())
            inside it, remove the left key, remove it from the store
                if the curr usage store got empty, remove it


keep track of the min_frequence
    it will always go back to 1 when you evict something (a new item would be being added)
    when you update an item, if it is the only one with min frequence, just make min_freq += 1 to follow it.

the sorted dict is a problem (insert time O(logn))
maybe have a list

usage_store: List[int, OrderedDict[int, int]]

1: [1]




"""
