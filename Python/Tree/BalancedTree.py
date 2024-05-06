class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left),height(root.right))
        if not root:
            return True
        x = abs(height(root.right)-height(root.left))
        if x!=1 and x!=0:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)