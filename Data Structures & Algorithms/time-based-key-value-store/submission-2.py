import heapq
class kvStoreValue:
    def __init__(self):
        self.times = []
        self.timeToValue = {}

class TimeMap:
    def __init__(self):
        self.kvStore= {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kvStore:
            self.kvStore[key].times.append(timestamp)
            # no need to sort since all timestamps of "set" are strictly increasing
            # => already sorted
            # self.kvStore[key].times.sort()
            self.kvStore[key].timeToValue[timestamp] = value
        else:
            newElement = kvStoreValue()
            newElement.times.append(timestamp)
            newElement.timeToValue[timestamp]=value
            self.kvStore[key] = newElement

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvStore:
            return ""
        cur = self.kvStore[key]
        if timestamp in cur.timeToValue:
            return cur.timeToValue[timestamp]
        # do binary search to find max timestamp_prev
        l, r = 0, len(cur.times)-1
        targetTime = float("-inf")
        while l <= r:
            m = (l + r) // 2
            if cur.times[m] > timestamp:
                r = m - 1
            else:
                targetTime = max(targetTime, cur.times[m])
                l = m + 1
        return cur.timeToValue[targetTime] if targetTime != float("-inf") else ""

        
