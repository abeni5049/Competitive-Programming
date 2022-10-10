# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node,ancestors,sum_):
            nonlocal res
            if not node or not node.left and not node.right:
                if node and sum_+node.val == targetSum:
                    res.append(ancestors+[node.val])
                return
            ans = None
            l = dfs(node.left,ancestors+[node.val],sum_+node.val)
            r = dfs(node.right,ancestors+[node.val],sum_+node.val)
            return 
        dfs(root,[],0)
        return res
