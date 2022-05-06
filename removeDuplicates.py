class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = {}
        for i,char in enumerate(s):
            if stack and s[stack[-1]] == char: count[i] = count[stack[-1]] + 1
            else: count[i] = 1
            stack.append(i)
            if count[i] == k:
                cnt = k
                while cnt:
                    stack.pop()
                    cnt -=1
        res = []
        for ind in stack:
            res.append(s[ind])
        return ''.join(res)
            
