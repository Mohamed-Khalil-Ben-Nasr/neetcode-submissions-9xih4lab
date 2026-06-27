class TimeMap:
    def __init__(self):
        self.kvStore= {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # no need to sort since all timestamps of "set" are strictly increasing
        # => already sorted
        if key not in self.kvStore:
            self.kvStore[key] = []
        self.kvStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvStore:
            return ""

        # if target timestamp doesnt exist
        # find the max timestamp closest to target timestamp
        res = ""
        curMaxTime = float("-inf")
        l, r = 0, len(self.kvStore[key])-1
        while l <= r:
            cur = (l+r) // 2
            if self.kvStore[key][cur][0] == timestamp:
                curMaxTime = self.kvStore[key][cur][0]
                res = self.kvStore[key][cur][1]
                break
            elif self.kvStore[key][cur][0] > timestamp:
                r = cur - 1
            else:
                if curMaxTime < self.kvStore[key][cur][0]:
                    curMaxTime = self.kvStore[key][cur][0]
                    res = self.kvStore[key][cur][1]
                l = cur + 1
        return res
