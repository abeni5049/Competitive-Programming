# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        def dfs(root):
            if not root: return False
            if root.val == subRoot.val and isSame(root,subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
            
        
        def isSame(root,subRoot):
            if not root and not subRoot: return True
            if not root and subRoot or root and not subRoot: return False
            if root.val != subRoot.val: return False
            return isSame(root.left,subRoot.left) and isSame(root.right,subRoot.right)
        
        return dfs(root)
