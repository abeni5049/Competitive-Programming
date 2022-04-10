class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix), len(matrix[0])
        cache = {}
        def dp(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i == n or j == m: return 0
            down = dp(i+1,j)
            right = dp(i,j+1)
            diag = dp(i+1,j+1)
            cache[(i,j)] = 1 + min(down,right,diag) if matrix[i][j] == "1" else 0
            return cache[(i,j)] 
        dp(0,0)
        return max(cache.values())**2
