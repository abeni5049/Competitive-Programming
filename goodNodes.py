# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_):
            if not root: return 0
            max_ = max(max_,root.val)
            l = dfs(root.left,max_)
            r = dfs(root.right,max_)
            return l+r+1 if root.val >= max_ else l+r
        return dfs(root,float('-inf'))
