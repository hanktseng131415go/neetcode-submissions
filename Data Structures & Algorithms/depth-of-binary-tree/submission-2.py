# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            depth+=1

        return depth

        # Iterative DFS (Stack)
        # time: n
        # space: n
        stack = [[root, 1]]
        out = 0
        while stack:
            node, depth = stack.pop()
            if node:
                out = max(out, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return out
        
        # Recursive DFS
        # time: n
        # space: n
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
       