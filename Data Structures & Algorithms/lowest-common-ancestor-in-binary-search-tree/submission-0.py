# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.min_h = float('inf')
        self.min_n = None

        self.layer(root)

        return self.min_n
        
    def layer(self, node):

        if not node:
            return 0

        l = self.layer(node.left)
        r = self.layer(node.right)
        h = 1 + max(l, r)
        
        if min(p.val, q.val) <= node.val <= max(p.val, q.val) and -h <= self.min_h:
            self.min_h = min(self.min_h, -h)
            self.min_n = node

        return h
        