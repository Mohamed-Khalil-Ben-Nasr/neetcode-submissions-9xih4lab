from collections import deque
class Node:
    def __init__(self, key: int, value:int):
        self.prev = None
        self.nxt = None
        self.value = value
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.keyToNode = {}
        # head and tail are fixed dummy nodes
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        print("operation: get ", key)
        if key in self.keyToNode:
            # find the node corresponding to the current key
            cur = self.keyToNode[key]
            # remove current node from its current position in the DLL
            # by removing its connections with its neighbors
            cur.prev.nxt = cur.nxt
            print("head.nxt ", self.head.nxt.key)
            cur.nxt.prev = cur.prev
            # update its position in the doubly linked list
            # most recently used => make it the tail
            # linked list is ordered from least recently used to most recently used
            cur.prev = self.tail.prev
            cur.nxt = self.tail
            self.tail.prev.nxt = cur
            self.tail.prev = cur
            print("since i got this key ", key)
            print("tail.prev needs to match ", self.tail.prev.key)
            print("current head.nxt needs to be different ", self.head.nxt.key)
            return cur.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        print("operation: put key ", key)
        # if cache is full
        if key not in self.keyToNode and len(self.keyToNode.keys()) == self.capacity:
            print(self.keyToNode)
            print("current head ", self.head.nxt.key)
            # remoxve head.next which corresponds to least recently used keyValue pair
            tmp = self.head.nxt
            self.head.nxt = self.head.nxt.nxt
            self.head.nxt.prev = self.head
            # update hashmap
            del self.keyToNode[tmp.key]
            print("just deleted node corresponding to ", tmp.key)
        cur = None
        if key not in self.keyToNode:
            newNode = Node(key, value)
            newNode.prev = self.tail.prev
            newNode.nxt = self.tail
            cur = newNode
        else:
            cur = self.keyToNode[key]
            cur.value = value
            cur.prev.nxt = cur.nxt
            cur.nxt.prev = cur.prev
        # now put node corresponding to new or recently used key-value pair at the end of the DLL
        cur.nxt = self.tail
        cur.prev = self.tail.prev
        self.tail.prev.nxt = cur
        self.tail.prev = cur
        self.keyToNode[key] = cur





            
        
