class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dfs(chars,curr):
            if len(chars) == n: return 0
            if len(chars) > n: return float('inf')
            copy = 1+dfs(chars,chars) if chars != curr else float('inf')
            paste = 1+dfs(chars+curr,curr) if curr != '' else float('inf')
            return min(copy,paste)
        return dfs('A','')
