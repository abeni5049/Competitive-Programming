class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        P = [0]
        for i in nums:
            P.append(P[-1] + i)

        res = len(nums)+1
        queue = deque()
        for y, Py in enumerate(P):
            while queue and Py <= P[queue[-1]]:
                queue.pop()
                
            while queue and Py - P[queue[0]] >= k:
                res = min(res, y - queue.popleft())

            queue.append(y)

        return res if res <= len(nums) else -1
        
