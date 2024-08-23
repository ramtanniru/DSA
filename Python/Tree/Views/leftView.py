def LeftView(root):
    def helper(root,level):
        nonlocal maxLevel,res
        if not root:
            return
        if level>maxLevel:
            maxLevel = level
            res.append(root.data)
        helper(root.left,level+1)
        helper(root.right,level+1)
    maxLevel = 0
    res = []
    helper(root,1)
    return res 