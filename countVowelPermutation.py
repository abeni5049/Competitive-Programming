class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = 0
        memo = {}
        for char in 'aeiou':
            count += self.dfs(1,char,n,memo)
        return count%(10**9+7)
    
    def dfs(self,lenOfString,prevCharacter,n,memo):
        if lenOfString == n: return 1
        if (lenOfString,prevCharacter) in memo: return memo[(lenOfString,prevCharacter)]
        res = 0
        if prevCharacter == 'a':
            res += self.dfs(lenOfString+1,'e',n,memo)
        elif prevCharacter == 'e':
            res += self.dfs(lenOfString+1,'a',n,memo) + self.dfs(lenOfString+1,'i',n,memo)
        elif prevCharacter == 'i':
            for char in 'aeou':
                res += self.dfs(lenOfString+1,char,n,memo)
        elif prevCharacter == 'o':
            res += self.dfs(lenOfString+1,'i',n,memo) + self.dfs(lenOfString+1,'u',n,memo)
        elif prevCharacter == 'u':
            res += self.dfs(lenOfString+1,'a',n,memo)
        memo[(lenOfString,prevCharacter)] = res
        return res
