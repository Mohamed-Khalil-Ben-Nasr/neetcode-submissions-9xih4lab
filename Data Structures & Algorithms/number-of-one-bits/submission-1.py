class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        # str.count(substring)
        return b.count("1")