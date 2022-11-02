class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (1<<i) & n != 0:
                count += 1
        return count
