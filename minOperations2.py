class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log[0] != '.':
                count += 1
            if log == '../':
                count -= 1
            count = max(count,0)
        return count
