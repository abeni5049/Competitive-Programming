# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        roots = []
        def dfs(root,is_parent_deleted):
            if not root: return None
            is_deleted = root.val in to_delete
            if is_parent_deleted and not is_deleted: roots.append(root)
            root.left = dfs(root.left,is_deleted)
            root.right = dfs(root.right,is_deleted)
            return None if is_deleted else root
        dfs(root,True)
        return roots
