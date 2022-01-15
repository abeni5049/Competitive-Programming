class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        count = 0
        for num in nums:
            while maxd and num > maxd[-1]: 
                maxd.pop()
            while mind and num < mind[-1]: 
                mind.pop()
            maxd.append(num)
            mind.append(num)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[count]: 
                    maxd.popleft()
                if mind[0] == nums[count]: 
                    mind.popleft()
                count += 1
        return len(nums) - count
