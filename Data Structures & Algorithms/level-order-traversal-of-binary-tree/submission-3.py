# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        out = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            len_q = len(queue)
            level = []
            for i in range(len_q):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                out.append(level)
        
        return out


        # Depth First Search
        # time: n
        # space: n
        out = []
        def dfs(node, d):
            if not node:
                return None
            
            if d == len(out):
                out.append([])
            
            out[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)

        dfs(root, 0)

        return out

        # my solution: dfs + hash map
        # time: n
        # space: n
        out = {}

        def dfs(node, d):
            
            if not node:
                return 0

            if d not in out:
                out[d] = []
            
            out[d].append(node.val)

            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        out = [out[d] for d in sorted(out.keys())]

        return out