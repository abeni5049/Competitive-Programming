class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        lookup = {}
        def dp(i,j):
            if (i,j) in lookup: return lookup[(i,j)]
            if i >= len(text1) or j >= len(text2): return 0
            lookup[(i,j)] = 1 + dp(i+1,j+1) if text1[i] == text2[j] else max(dp(i+1,j),dp(i,j+1))
            return lookup[(i,j)]
        
        return dp(0,0)
