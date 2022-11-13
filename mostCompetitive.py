class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i,num in enumerate(nums):
            while stack and num < stack[-1] and (len(nums)-i)+len(stack) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
