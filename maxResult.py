class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque([0])
        for i in range(1, len(nums)):
            nums[i] = nums[q[0]] + nums[i]
            while q and nums[q[-1]] <= nums[i]: q.pop()  
            q.append(i)
            if i - q[0] >= k: 
                q.popleft()
        return nums[len(nums)-1]
