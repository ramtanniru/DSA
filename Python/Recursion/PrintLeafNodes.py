def printLeafNodesFromLeftToRight(root):
    if root==None:
        return -1
    if root.left==None and root.right==None:
        print(root.val)
    printLeafNodesFromLeftToRight(root.left)
    printLeafNodesFromLeftToRight(root.right)