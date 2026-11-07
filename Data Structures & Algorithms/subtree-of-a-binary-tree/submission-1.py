# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_same(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque([root])

        res = False

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if self.is_same(node, subRoot):
                    res = True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        
        return res