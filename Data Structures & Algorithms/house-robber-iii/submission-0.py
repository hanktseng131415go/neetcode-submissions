# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if not node:
                return [0, 0]
            
            ls = dfs(node.left)
            rs = dfs(node.right)
            w_n = node.val + ls[1] + rs[1]
            wo_n = max(ls) + max(rs)

            return [w_n, wo_n]
        
        return max(dfs(root))