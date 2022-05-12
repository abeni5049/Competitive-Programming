class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:return 0
        return haystack.index(needle) if needle in haystack else -1
