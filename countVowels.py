class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        for i,char in enumerate(word):
            if char in 'aeiou':
                res += (i+1)*(len(word)-i)
        return res
