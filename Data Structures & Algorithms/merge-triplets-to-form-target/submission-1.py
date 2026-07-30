class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:     
        a = b = c = 0
        for x, y, z in triplets:
            # skip or else it will never go down to target cuz it will
            # always pick the max
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            a = max(a, x)
            b = max(b, y)
            c = max(c, z)
            if (a,b,c) == tuple(target):
                return True
        return False
        