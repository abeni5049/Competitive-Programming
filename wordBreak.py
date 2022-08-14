class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        words = set(wordDict)
        for i in range(len(s)):
            if i == 0 or dp[i-1]:
                for j in range(i,len(s)):
                    if s[i:j+1] in words:
                        dp[j] = True
        return dp[-1]
