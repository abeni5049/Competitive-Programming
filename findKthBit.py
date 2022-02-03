class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev_inv(n):
            if n == 1: return "0"
            y = rev_inv(n-1)
            rev = list(y[::-1])
            for i in range(len(rev)):
                if rev[i] == '0':
                    rev[i] = '1'
                elif rev[i] == '1':           
                    rev[i] = '0'              
            return  y + "1" + ''.join(rev)
        return rev_inv(n)[k-1]
