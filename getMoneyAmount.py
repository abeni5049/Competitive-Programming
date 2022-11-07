class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(l,r):
            if l >= r: return 0
            min_cost = float('inf')
            for k in range(l,r+1):
                min_cost = min(min_cost,k+max(dp(l,k-1),dp(k+1,r)))
            return min_cost
        return dp(1,n)
