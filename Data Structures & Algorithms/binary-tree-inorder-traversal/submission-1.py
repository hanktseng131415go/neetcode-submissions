# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # 2. Iterative Depth First Search
        out, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            out.append(cur.val)
            cur = cur.right
        
        return out
        
        # # 1. Depth First Search
        # # time: n
        # # space: n
        # out = []
        
        # def recursion(node):
        #     if not node:
        #         return 
            
        #     recursion(node.left)
        #     out.append(node.val)
        #     recursion(node.right)
        
        # recursion(root)
        
        # return out