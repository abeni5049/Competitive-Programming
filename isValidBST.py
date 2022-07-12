# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root):
            if not root: return True,float('-inf'),float('inf')
            l = isValid(root.left)
            r = isValid(root.right)
            max_ = max(r[1],root.val)
            min_ = min(l[2],root.val)
            isvalid = root.val > l[1] and root.val < r[2] and l[0] and r[0]
            return isvalid,max_,min_
        
        return isValid(root)[0]
