# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: Both nodes are empty -> identical structure at this leaf
        if not p and not q:
            return True
        
        # Case 2: One is None and the other isn't, or node values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Case 3: Values match -> recursively check both left and right subtrees synchronously
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
