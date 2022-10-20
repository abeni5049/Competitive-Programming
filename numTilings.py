class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def dfs(n,state):
            if n == 1: return 1
            if n == 2: return 2
            if state == 0:
                return dfs(n-1,0) + dfs(n-2,0) + dfs(n-2,1) + dfs(n-2,2)
            elif state == 1:
                return dfs(n-1,0) + dfs(n-1,2)
            else:
                return dfs(n-1,0) + dfs(n-1,1) 
        return dfs(n,0) % (10**9+7)
