# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Hash Map + Depth First Search
        h_map = {}
        for i, v in enumerate(inorder):
            h_map[v] = i
        
        self.pre_i = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_i]
            root = TreeNode(root_val)
            self.pre_i += 1
            in_i = h_map[root_val]

            root.left = dfs(l, in_i-1)
            root.right = dfs(in_i+1, r)

            return root
        
        return dfs(0, len(preorder)-1)

        # Depth First Search
        # time: n
        # space: n**2
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root