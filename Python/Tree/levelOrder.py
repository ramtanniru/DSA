class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [[root]]
        ans = [[root.val]]
        while q:
            temp = q.pop()
            res = []
            for i in temp:
                if i.left:
                    res.append(i.left)
                if i.right:
                    res.append(i.right)
            if res:
                q.append(res)
            val = [i.val for i in res]
            ans.append(val)
        return ans[:-1] 