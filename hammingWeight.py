class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryNumber = self.integerToBinary(n)
        return self.countOneBits(binaryNumber)
        
    def integerToBinary(self, number):
        binaryNumber = ''
        while number != 0:
            binaryNumber += str(number % 2)
            number //= 2
        return binaryNumber[::-1]
    
    def countOneBits(self, binaryNumber):
        count = 0
        for char in binaryNumber:
            count += int(char)
        return count
