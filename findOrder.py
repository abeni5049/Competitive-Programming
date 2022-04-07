class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjacents = {}
        for course,pre in prerequisites:
            indegree[course] += 1
            adjacents[pre] = adjacents.get(pre,[]) + [course]
        
        queue = deque()
        for course,degree in enumerate(indegree):
            if degree == 0:
                queue.append(course)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            adjs = adjacents.get(course,[])
            for adj in adjs:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        return res if len(res) == numCourses else []
            
            
