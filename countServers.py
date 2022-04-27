class UnionFind:
    def __init__(self,size):
        self.roots = [i for i in range(size)]
    
    def find(self,x):
        if x == self.roots[x] : return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.roots[rooty] = rootx 
            
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        uf = UnionFind(n*m)
        def encode(r,c):
            return m*r + c
        rows = defaultdict(list)
        cols = defaultdict(list)
        for i in range(n):
            for j in range(m):  
                if grid[i][j] == 1:
                    rows[i].append(encode(i,j))
                    cols[j].append(encode(i,j))
        
        for row,lists in rows.items():
            for i in range(1,len(lists)):
                uf.union(lists[i-1],lists[i])
        
        for col,lists in cols.items():
            for i in range(1,len(lists)):
                uf.union(lists[i-1],lists[i])
                        
        for i in range(n):
            for j in range(m):
                uf.roots[encode(i,j)] = uf.find(encode(i,j))
        
        count = defaultdict(int)
        for root in uf.roots:
            count[root] += 1
        
        res = 0
        for root,freq in count.items():
            if freq >= 2:
                res += freq
        return res
        
                
