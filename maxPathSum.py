# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')
        def maxSum(root):
            nonlocal res
            if not root: return float('-inf')
            max_l = maxSum(root.left)
            max_r = maxSum(root.right)
            max_ = max(root.val,max_l+root.val,max_r+root.val)
            res = max(res,max_,max_l+max_r+root.val)
            return max_
        maxSum(root)
        return res
