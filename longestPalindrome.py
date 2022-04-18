class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        even,odd = '',''
        for i in range(len(s)):    
            
            #even length palindrome
            l,r = i,i+1
            st = ''
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    st = s[l] + st + s[r]
                else: break
                l -= 1
                r += 1
            if len(st) > len(even): even = st
                
            #odd length palindrom
            l,r = i-1,i+1
            st = s[i]
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    st = s[l] + st + s[r]
                else: break
                l -= 1
                r += 1
            if len(st) > len(odd): odd = st
                
        return even if len(even) > len(odd) else odd
            
