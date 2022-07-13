# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        seen = set()
        def buildTree(inorder):
            if not inorder: return None
            if len(inorder) == 1:
                seen.add(inorder[0])
                return TreeNode(inorder[0])
            root, val = None, None
            for num in preorder:
                if num not in seen:
                    root = TreeNode(num)
                    val = num
                    break
            if root:
                seen.add(val)
                ind = inorder.index(val)
                root.left = buildTree(inorder[:ind])
                root.right = buildTree(inorder[ind+1:])
            return root
        return buildTree(inorder)
        
        
        
