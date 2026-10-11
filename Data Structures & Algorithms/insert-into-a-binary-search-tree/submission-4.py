# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # recursion
        # time: n
        # space: h
        def dfs(node, val):
            if not node:
                node = TreeNode(val=val)
                return node
            
            if val < node.val:
                node.left = dfs(node.left, val)
            elif node.val < val:
                node.right = dfs(node.right, val)

            return node

        root = dfs(root, val)

        return root

        # my solution: iteration
        # time: n
        # space: 1

        if not root:
            root = TreeNode(val=val)
            return root

        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val=val)
                    return root
                node = node.right

            elif val < node.val:
                if not node.left:
                    node.left = TreeNode(val=val)
                    return root
                node = node.left
        

        return root
