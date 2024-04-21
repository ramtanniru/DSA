# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(root,stk=[]):
            if root==None:
                return 
            stk.append(str(root.val))
            if root.left==None and root.right==None:
                self.res.append("->".join(stk))
                if stk:
                    stk.pop()
                return
            if root.left:
                traverse(root.left,stk)
            if root.right:
                traverse(root.right,stk)
            if stk:
                stk.pop()
            return
        traverse(root)
        return self.res