class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        limit = 10**9+7
        maxNum = 2**p -1
        res = 1
        if maxNum % 2:
            res *= maxNum
        res *= pow((maxNum -1) , (maxNum //2),limit)
        return res % limit
