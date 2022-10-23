class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def dfs(i,j):
            if i == len(s1) or j == len(s2): return 0
            if s1[i] == s2[j]:
                return 2*ord(s1[i])+dfs(i+1,j+1)
            return max(dfs(i+1,j),dfs(i,j+1))
        total = 0
        for char in s1+s2:
            total += ord(char)
        return total-dfs(0,0)
