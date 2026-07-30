class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence = {}
        for i, c in enumerate(s):
            lastOccurence[c] = i
        
        res = []
        end = -1
        size = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastOccurence[c])
            if i == end:
                res.append(size)
                size = 0
        return res