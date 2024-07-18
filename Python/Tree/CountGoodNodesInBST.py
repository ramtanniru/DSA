class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(root,maX = float('-inf'),path = []):
            nonlocal res
            if not root:
                return
            if root.val>=maX:
                res.append(root.val)
                dfs(root.left,root.val,path+[root.val])
                dfs(root.right,root.val,path+[root.val])
            else:
                dfs(root.left,maX,path+[root.val])
                dfs(root.right,maX,path+[root.val])
        dfs(root)
        return len(res) 