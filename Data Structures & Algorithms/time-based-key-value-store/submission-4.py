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
        values = self.kvStore[key]
        l, r = 0, len(values)-1
        while l <= r:
            m = (l+r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                # we can find an even bigger timestamp thats closer to target T
                # on the right side
                l = m + 1
            else:
                r = m - 1
            
        return res
