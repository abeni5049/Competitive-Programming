class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegrees = [0] * numCourses
        outgoing = defaultdict(set)
        pre = defaultdict(set)
        for c,p in prerequisites:
            indegrees[c] += 1
            pre[c].add(p)
            outgoing[p].add(c)
        
        queue = deque()
        for i,indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        while queue:
            cor = queue.pop()
            courses = outgoing[cor]
            pres = pre[cor]
            for cr in courses:
                for t in pres:
                    pre[cr].add(t)
                indegrees[cr] -= 1
                if indegrees[cr] == 0:
                    queue.append(cr)
        res = []
        for c,p in queries:
            if p in pre[c]:
                res.append(True)
            else:
                res.append(False)
        return res
