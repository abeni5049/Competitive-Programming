class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        @cache
        def dfs(i,j):
            if not(0<=i<n and 0<=j<m): return 0
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            max_len = 1
            for x, y in directions:
                x += i
                y += j
                if 0<=x<n and 0<=y<m and matrix[i][j] > matrix[x][y]:
                    max_len = max(max_len,dfs(x,y)+1)
            return max_len
        max_len = 1
        for i in range(n):
            for j in range(m):
                max_len = max(max_len,dfs(i,j))
        return max_len
