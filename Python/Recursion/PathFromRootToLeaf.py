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
                stk.pop()
                return
            traverse(root.left,stk)
            traverse(root.right,stk)
            stk.pop()
            return
        traverse(root)
        return self.res