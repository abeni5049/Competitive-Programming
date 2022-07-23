"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        nodes = {}
        seen = set()
        queue = deque() 
        queue.append(node)
        seen.add(node)
        while queue:
            n = queue.popleft()
            newNode = nodes[n.val] if n.val in nodes else Node(val=n.val) 
            nodes[n.val] = newNode
            for m in n.neighbors:
                if m not in seen :
                    queue.append(m)
                    seen.add(m)
                nd = nodes[m.val] if m.val in nodes else Node(val=m.val) 
                nodes[m.val] = nd
                newNode.neighbors.append(nd)
        return nodes.get(1,None)
