# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # iteration
        out = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                out.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        
        return out

        # recursion
        # time: n
        # space: n
        out = []
        
        def preorder(node):

            if not node:
                return
            
            out.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        return out