# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Breadth First Search
        q = collections.deque()
        q.append((root, -float('inf'), float('inf')))
        while q:
            node, l, r = q.popleft()
            if not l < node.val < r:
                return False
            
            if node.left:
                q.append((node.left, l, node.val))
            
            if node.right:
                q.append((node.right, node.val, r))
            
        return True
        
        # Depth First Search
        # time: n
        # space: h
        def dfs(node, l=-float('inf'), u=float('inf')):

            if not node:
                return True
            
            if not (l < node.val < u):
                return False

            return dfs(node.left, l, node.val) and dfs(node.right, node.val, u)
        
        return dfs(root)
            
