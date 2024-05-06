class Solution:
    def isSame(self,p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val==q.val and self.isSame(p.left,q.left) and self.isSame(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            if not subRoot:
                return True
            return False
        if self.isSame(root,subRoot):
            return True
        if self.isSame(root.left,subRoot) or self.isSame(root.right,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)