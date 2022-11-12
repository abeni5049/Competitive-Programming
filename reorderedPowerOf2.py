class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = 1
        while len(str(num)) <= len(str(n)):
            if len(str(num)) == len(str(n)) and int(''.join(sorted(str(num)))) == int(''.join(sorted(str(n)))):
                return True
            num *= 2
        return False
                                    
        
