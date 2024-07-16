class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root):
            nonlocal res
            if not root:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        res = []
        inOrder(root)
        if len(res)<2:
            return True
        i,j = 0,1
        while j<len(res):
            if res[i]>=res[j]:
                return False
            i += 1
            j += 1
        return True 