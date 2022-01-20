class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        def pow(num,p,limit):
            if p == 0:
                return 1
            if p == 1:
                return num
            res = pow(num,p//2,limit)**2
            if p % 2:
                res *= num
            return res % limit
        
        limit = 10**9+7
        maxNum = 2**p -1
        res = 1
        if maxNum % 2:
            res *= maxNum
        res *= pow((maxNum -1) , (maxNum //2),limit)
        return res % limit
