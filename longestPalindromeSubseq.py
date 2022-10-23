class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i,j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return 2+dfs(i+1,j-1)
            else:
                return max(dfs(i+1,j),dfs(i,j-1))
            
        return dfs(0,len(s)-1)
