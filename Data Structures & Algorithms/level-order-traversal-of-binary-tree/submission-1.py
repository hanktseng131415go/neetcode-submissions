# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = {}

        def dfs(node, d):
            
            if not node:
                return 0

            if d not in out:
                out[d] = []
            
            out[d].append(node.val)

            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        out = [out[d] for d in sorted(out.keys())]

        return out