class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        max_value, sum_ = 0, 0
        while satisfaction and sum_ + satisfaction[-1] > 0:
            sum_ += satisfaction.pop()
            max_value += sum_
        return max_value
    
