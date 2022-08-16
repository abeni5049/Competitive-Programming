class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        row = [1,1]
        for i in range(2,rowIndex+1):
            temp = [1] + row
            for j in range(1,len(temp)-1):
                temp[j] = row[j] + row[j-1]
            row = temp
        return row
