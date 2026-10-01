# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out, stack = [], []
        node = root
        while node or stack:
            if node:
                out.append(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
                
        out.reverse()
        return out

        # recursion
        # time: n
        # space: n
        out = []

        def recursion(node):

            if not node:
                return 
            
            recursion(node.left)
            recursion(node.right)
            out.append(node.val)

        recursion(root)

        return out
