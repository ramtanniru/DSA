class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root,val,res=[],path=[]):
            if not root:
                return res
            if root.val==val:
                path += [root]
                res = path
                return res
            if not res:
                res = findPath(root.left,val,res,path+[root])
            if not res:
                res = findPath(root.right,val,res,path+[root])
            return res 
        pPath = findPath(root,p.val)
        qPath = findPath(root,q.val)
        i = -1
        while i<len(pPath)-1 and i<len(qPath)-1:
            if pPath[i+1]!=qPath[i+1]:
                break
            i += 1
        return pPath[i] 