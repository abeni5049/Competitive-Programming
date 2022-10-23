class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i,j):
            if j == len(t): return 1
            if i == len(s): return 0
            pick = dfs(i+1,j+1) if s[i] == t[j] else 0
            dont_pick = dfs(i+1,j)
            return pick + dont_pick
        return dfs(0,0)
