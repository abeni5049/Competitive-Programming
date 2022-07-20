class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def pre(word1,word2):
            i,j=0,0
            res = []
            l = min(len(word1),len(word2))
            for i in range(l):
                if word1[i] == word2[i]: res.append(word1[i])
                else: break
            return ''.join(res)
        res = strs[0]
        for i in range(1,len(strs)):
            res = pre(res,strs[i])
        return res
        
