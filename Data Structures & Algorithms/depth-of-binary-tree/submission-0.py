# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        max_depth = 0

        def helper(root, depth):
            nonlocal max_depth
            ## base
            if not root:return

            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

            max_depth = max(max_depth, depth)

        
        helper(root, 1)

        return max_depth

