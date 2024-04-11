class Solution:
    def invert(self,root):
            if root is None:
                return
            self.invertTree(root.left)
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        self.invert(curr)
        return root