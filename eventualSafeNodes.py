class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegrees = [0] * len(graph)
        outgoing = {}
        for i,edges in enumerate(graph):
            indegrees[i] = len(edges)
            for edge in edges:
                outgoing[edge] = outgoing.get(edge,[]) + [i]
        
        queue = deque()
        for i,indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            nodes = outgoing.get(node,[])
            for node in nodes:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
        return sorted(res)
