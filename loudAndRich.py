class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        answer = [ i for i in range(len(quiet))]
        indegrees = [0] * len(quiet)
        outgoings = defaultdict(list)
        for rich,poor in richer:
            indegrees[poor] += 1
            outgoings[rich].append(poor)
                
        queue = deque()
        for i in range(len(quiet)):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            person = queue.popleft()
            for p in outgoings[person]:
                indegrees[p] -= 1
                answer[p] = answer[person] if quiet[answer[person]] < quiet[answer[p]] else answer[p]
                if indegrees[p] == 0:
                    queue.append(p)
            
        return answer
                                    
