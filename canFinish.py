class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjacent = {}
        for course,pre in prerequisites:
            indegree[course] += 1
            adjacent[pre] = adjacent.get(pre,[]) + [course]
            
        queue = deque()  
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            adjacents = adjacent.get(course,[])
            for adj in adjacents:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        return len(res) == numCourses
