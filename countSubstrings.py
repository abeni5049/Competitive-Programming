class Solution:
    def countSubstrings(self, s: str) -> int:
        count= 0
        for i in range(len(s)):
            #even
            l,r = i,i+1
            while l>=0 and r<len(s):
                if s[l] == s[r]: 
                    count += 1
                else: break
                l,r = l-1,r+1
            #odd
            l,r=i-1,i+1
            count += 1
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    count += 1
                else: break
                l,r = l-1,r+1
        return count
