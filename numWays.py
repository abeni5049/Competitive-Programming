class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dfs(i,steps):
            if not(0<=i<arrLen): return 0
            if steps == 0: return 1 if i == 0 else 0
            return dfs(i+1,steps-1)+dfs(i-1,steps-1)+dfs(i,steps-1)
        return dfs(0,steps)%(10**9+7)
