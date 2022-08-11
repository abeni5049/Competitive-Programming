class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        seen_pac = set()
        def dfs_pac(prev,i,j):
            if (i,j) in seen_pac: return
            if not(0<=i<len(heights) and 0<=j<len(heights[0])): return
            if heights[i][j] < prev: return
            seen_pac.add((i,j))
            prev = heights[i][j]
            dfs_pac(prev,i+1,j)
            dfs_pac(prev,i-1,j)
            dfs_pac(prev,i,j-1)
            dfs_pac(prev,i,j+1)
        
        res = []
        seen_atl = set()
        def dfs_atl(prev,i,j):
            if (i,j) in seen_atl: return
            if not(0<=i<len(heights) and 0<=j<len(heights[0])): return
            if heights[i][j] < prev: return
            if (i,j) in seen_pac: res.append([i,j])
            seen_atl.add((i,j))
            prev = heights[i][j]
            dfs_atl(prev,i-1,j)
            dfs_atl(prev,i+1,j)
            dfs_atl(prev,i,j-1)
            dfs_atl(prev,i,j+1)
        
        for i in range(len(heights)):
            dfs_pac(float('-inf'),i,0)
        
        for j in range(len(heights[0])):
            dfs_pac(float('-inf'),0,j)
        
        for i in range(len(heights)):
            dfs_atl(float('-inf'),i,len(heights[0])-1)
        
        for j in range(len(heights[0])):
            dfs_atl(float('-inf'),len(heights)-1,j)
        
        return res
