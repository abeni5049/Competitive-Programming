class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        uf = UnionFind(n*m)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if j+1 < m and grid[i][j+1] == 1:
                        uf.union(i*m+j,i*m+(j+1))
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        uf.union(i*m+j,i*m+(j-1))
                    if i+1<n and grid[i+1][j] == 1:
                        uf.union(i*m+j,(i+1)*m+j)
                    if i-1>= 0 and grid[i-1][j] == 1:
                        uf.union(i*m+j,(i-1)*m+j)
                        
        area = {}               
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    root = uf.find(i*m+j)
                    area[root] = area.get(root,0) + 1
        return area[sorted(area.keys(), key = lambda x: area[x],reverse=True)[0]] if area else 0
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
