class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)
        words.sort(key=lambda x: len(x))
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if self.checkPred(words[j],words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def checkPred(self,word1,word2):
        if len(word2) != len(word1)+1: return False
        count, i, j = 0, 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i, j = i+1, j+1
            else:
                count += 1
                j += 1
        return True if (count == 1 and i == len(word1) and j == len(word2)) or word1 == word2[:len(word1)] else False  
