class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            nonlocal res
            if not root:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        res = []
        inOrder(root)
        i = 0
        while i<k-1:
            i += 1
        return res[i] 