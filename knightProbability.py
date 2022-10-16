class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(i,j,k):
            if not(0<=i<n and 0<=j<n): return 0
            if not k: return 1
            directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
            res = 0
            for x,y in directions:
                if k:
                    res += dfs(i+x,j+y,k-1)
            return res
        return dfs(row,column,k)/8**k
    
    
