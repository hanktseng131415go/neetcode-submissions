# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # # recursion
        # # time: n
        # # space: h
        # if not root:
        #     root = TreeNode(val=val)
        #     return root
        
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)

        # return root

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
