class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dfs(n,target):
            if n == 0: return 1 if target == 0 else 0
            if target < 0: return 0
            res = 0
            for i in range(1,k+1):
                res += dfs(n-1,target-i)
            return res
        return dfs(n,target)%(10**9+7)
    
    
    
