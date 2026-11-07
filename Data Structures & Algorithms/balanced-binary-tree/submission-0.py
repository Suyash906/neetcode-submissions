# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        result = True

        def helper(root, depth):
            nonlocal result
            if not root:
                return depth
            
            left = helper(root.left, depth + 1) if root.left else depth
            right = helper(root.right, depth + 1) if root.right else depth

            if abs(left - right) > 1:
                result = False

            return max(left, right)

        _= helper(root, 0)

        return result