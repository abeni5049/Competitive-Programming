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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf  = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    isConnected[j][i] = 0
                    uf.union(i,j)
        roots = set()
        for x in range(len(isConnected)):
            roots.add(uf.find(x))
        return len(roots)
        
