class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a=b=c=l=r=res=0
        while r < len(s):
            if s[r] == 'a': a+=1
            elif s[r] == 'b': b+=1
            elif s[r] == 'c': c+=1
            while a and b and c:
                res += len(s)-r
                if s[l] == 'a': a-=1
                elif s[l] == 'b': b-=1
                elif s[l] == 'c': c-=1
                l += 1
            r += 1
        return res
