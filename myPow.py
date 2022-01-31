class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x,-n)
        if n == 0: return 1
        if n == 1: return x
        y = self.myPow(x,n//2)
        res = y*y
        if n % 2: 
            res *= x
        return res
    
