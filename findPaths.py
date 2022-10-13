class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i,j,move):
            if not(0<=i<n and 0<=j<m): return 1
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            res = 0
            for x,y in directions:
                if move:
                    res += dfs(i+x,j+y,move-1)
            return res 
        return dfs(startRow,startColumn,maxMove) % (10**9+7)

