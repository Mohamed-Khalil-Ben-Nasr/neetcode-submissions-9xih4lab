class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.prev = None
        self.nxt = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.nxt = self.head
        self.size = 0
    def delete(self,node):
        # remove from old pos
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        self.size -= 1
    def add(self, node):
        # move to head of the list
        tmp = self.head.prev
        self.head.prev = node
        node.nxt = self.head
        tmp.nxt = node
        node.prev = tmp
        self.size += 1
    def deleteLRU(self):
        self.delete(self.tail.nxt)   

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = float("inf")
        self.keyToNode = {}
        self.keyToFreq = {}
        self.freqToKeys = {}

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        curNode = self.keyToNode[key]
        print(self.keyToFreq)
        # remove key from old freq bucket
        oldFreq = self.keyToFreq[key]
        self.freqToKeys[oldFreq].delete(curNode)
        # update frequency
        self.keyToFreq[key] += 1
        newFreq = self.keyToFreq[key]
        # initialize freq bucket 
        if newFreq not in self.freqToKeys:
            self.freqToKeys[newFreq] = DoublyLinkedList()
        # add it to new freq bucket
        self.freqToKeys[newFreq].add(curNode)   
        # update minFreq
        if self.freqToKeys[oldFreq].size == 0:
            del self.freqToKeys[oldFreq]
            if oldFreq == self.minFreq:
                self.minFreq = newFreq
        return curNode.val

    def put(self, key: int, value: int) -> None:

        if key not in self.keyToNode:
            # eviction policy
            if self.size == self.capacity:
                # if one element => no tie => pop lfu
                # if same freq => pop lru
                curNode = self.freqToKeys[self.minFreq].tail.nxt
                curKey = curNode.key
                # delete corresponding node
                del self.keyToNode[curKey]
                # delete corresponding frequency mapping
                del self.keyToFreq[curKey]
                # delete Last Recently Used anyways
                self.freqToKeys[self.minFreq].deleteLRU()
                # if new DDL size == 0 => delete bucket
                if self.freqToKeys[self.minFreq].size == 0:
                    del self.freqToKeys[self.minFreq]
                self.size -= 1
            # create new key -> node mapping
            self.keyToNode[key] = Node()
            curNode = self.keyToNode[key]
            curNode.key = key
            curNode.val = value
            self.keyToNode[key] = curNode
            # initialize freq
            self.keyToFreq[key] = 1
            if 1 not in self.freqToKeys:
                self.freqToKeys[1] = DoublyLinkedList()
            # add node to freq bucket
            self.freqToKeys[1].add(curNode)
            # reset minFreq
            self.minFreq = 1
            # update size
            self.size += 1
        else:
            # update value
            curNode = self.keyToNode[key]
            curNode.val = value
            # remove key from old freq bucket
            oldFreq = self.keyToFreq[key]
            self.freqToKeys[oldFreq].delete(curNode)
            # add it to new freq bucket and update frequency
            self.keyToFreq[key] += 1
            newFreq = self.keyToFreq[key]
            if newFreq not in self.freqToKeys:
                self.freqToKeys[newFreq] = DoublyLinkedList()
            self.freqToKeys[newFreq].add(curNode)
            # delete oldFreq bucket
            if self.freqToKeys[oldFreq].size == 0:
                del self.freqToKeys[oldFreq]
                # update minFreq
                if oldFreq == self.minFreq:
                    self.minFreq = newFreq
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)