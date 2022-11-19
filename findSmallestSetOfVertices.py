class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for u, v in edges:
            indegrees[v] += 1
        vertices = []
        for vertex, indgree in enumerate(indegrees):
            if indgree == 0:
                vertices.append(vertex)
        return vertices
                
