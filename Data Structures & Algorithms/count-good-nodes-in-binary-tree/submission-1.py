# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Breadth First Search
        out = 0
        q = collections.deque()
        q.append((root, root.val))
        while q:
            node, max_v = q.popleft()
            if node.val >= max_v:
                max_v = node.val
                out += 1
            
            if node.left:
                q.append((node.left, max_v))

            if node.right:
                q.append((node.right, max_v))
        
        return out

        # Depth First Search
        # time: n
        # space: h
        def dfs(node, max_v):

            if not node:
                return 0

            good = 1 if node.val >= max_v else 0

            max_v = max(max_v, node.val)

            l = dfs(node.left, max_v)
            r = dfs(node.right, max_v)

            return good + l + r

        return dfs(root, root.val)

