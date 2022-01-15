class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        stack = []
        numberToRemove = k
        for n in num:
            while stack and stack[-1] >  n and numberToRemove:
                stack.pop()
                numberToRemove -= 1
            stack.append(n)
        res = ''.join(stack[:len(num)-k]).lstrip('0')
        return res if len(res) else "0"
    
