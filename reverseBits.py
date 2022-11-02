class Solution:
    def reverseBits(self, n: int) -> int:
        num, k = 0, 31
        while n != 0:
            num += (n&1)*2**k
            n >>= 1
            k -= 1
        return num
