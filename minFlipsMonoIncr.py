class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = s.count('0')
        min_flips = flips
        for char in s:
            flips = flips-1 if char == '0' else flips+1
            min_flips = min(min_flips,flips)
        return min_flips
                
            
