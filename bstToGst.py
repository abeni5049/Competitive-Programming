# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(root,sum_):
            if not root: return 0
            root_val = root.val
            r = dfs(root.right,sum_)
            root.val += sum_ + r
            l = dfs(root.left,root.val)
            return root_val+l+r
        dfs(root,0)
        return root
