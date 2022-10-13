class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i-1>=0:
                    val = matrix[i-1][j]
                    if j-1>=0:
                        val = min(val,matrix[i-1][j-1])
                    if j+1<m:
                        val = min(val,matrix[i-1][j+1])
                    matrix[i][j] += val
        return min(matrix[-1])
