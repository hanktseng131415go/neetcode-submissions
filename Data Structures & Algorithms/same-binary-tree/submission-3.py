
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.p_stack = []
        self.q_stack = []

        def p_dfs(node):
            
            if not node:
                self.p_stack.append(None)
                return None
            
            self.p_stack.append(node.val)
            p_dfs(node.left)
            p_dfs(node.right)

        def q_dfs(node):
            
            if not node:
                self.q_stack.append(None)
                return None
            
            self.q_stack.append(node.val)
            q_dfs(node.left)
            q_dfs(node.right)
        
        p_dfs(p), q_dfs(q)

        return self.p_stack == self.q_stack