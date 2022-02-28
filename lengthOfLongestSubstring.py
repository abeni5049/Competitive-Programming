class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        l = res = 0
        for r,char in enumerate(s):
            if char in letters and l <= letters[char]:
                l = letters[char] + 1
            else:
                res = max(res,r-l+1)
            letters[char] = r
        return res
