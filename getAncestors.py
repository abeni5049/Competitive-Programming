class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegrees = [0] * n
        outgoings = defaultdict(set)
        ancestors = defaultdict(set)
        for node1,node2 in edges:
            indegrees[node2] += 1
            outgoings[node1].add(node2)
        
        queue = deque()
        for i,indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            outs = outgoings[node]
            for out in outs:
                ancestors[out].add(node)
                for anc in ancestors[node]:
                    ancestors[out].add(anc)
                indegrees[out] -= 1
                if indegrees[out] == 0:
                    queue.append(out)
                    
        res = [[]] * n
        for node,ancestor in ancestors.items():
            res[node] = sorted(ancestor)
        
        return res
            
            
