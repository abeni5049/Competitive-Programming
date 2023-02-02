class Solution:
    def numberOfWays(self, s: str) -> int:
        pre0 = [0]
        pre1 = [0]
        zeros,ones=0,0
        for char in s:
            if char == '0': 
                zeros += 1
                pre0.append(pre0[-1]+1)
            else: pre0.append(pre0[-1])
            if char == '1':
                ones += 1
                pre1.append(pre1[-1]+1)  
            else: pre1.append(pre1[-1])
        res = 0
        for i,char in enumerate(s):
            if char == '0':
                if pre1[i] and ones-pre1[i]:
                    res += pre1[i]*(ones-pre1[i])
            else:
                if pre0[i] and zeros-pre0[i]:
                    res += pre0[i]*(zeros-pre0[i])
        return res
        
