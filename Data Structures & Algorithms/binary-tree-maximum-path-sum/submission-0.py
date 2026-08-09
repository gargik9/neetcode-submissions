# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        best = float("-inf")
        
        def dfs(node):

            if not node:
                return 0
                
            nonlocal best
            l = max(0,dfs(node.left))
            r = max(0,dfs(node.right))

            best = max(best,node.val+l+r)

            return node.val + max(l,r)

        dfs(root)
        return best        