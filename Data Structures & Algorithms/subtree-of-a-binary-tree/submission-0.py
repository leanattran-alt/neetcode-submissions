# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            return (
                p.val == q.val
                and isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )
        
        if not subRoot:
            return True

        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False