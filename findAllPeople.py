class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0,firstPerson)
        #sort meetings by meeting time
        meetings.sort(key=lambda x: x[2])
        meetings_at_time = defaultdict(list)
        for person1, person2, time in meetings:
            meetings_at_time[time].append((person1,person2))
        
        for current_time,current_meetings in meetings_at_time.items():
            for person1, person2 in current_meetings:
                uf.union(person1,person2)
            for person1, person2 in current_meetings:
                if not uf.isConnected(person1,0):
                    uf.parent[person1] = person1
                if not uf.isConnected(person2,0):
                    uf.parent[person2] = person2
                    
        people_with_secret = []
        for person in range(n):
            if uf.isConnected(0,person):
                people_with_secret.append(person)
                
        return people_with_secret
