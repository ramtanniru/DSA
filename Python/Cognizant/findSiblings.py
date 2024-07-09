# find siblings of a person when the family tree is given and root is start person of the family 
from collections import deque
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

Q = deque()

def insert(val,root):
    newNode = Tree(val)
    if Q:
        temp = Q[0]
    if not root:
        root = newNode
    elif not temp.left:
        temp.left = newNode
    elif not temp.right:
        temp.right = newNode
        Q.popleft()
    Q.append(newNode)
    return root

def buildTree(arr,root = None):
    for i in arr:
        root = insert(i,root)
    return root

def findSiblings(root,key):
    if not root:
        return -1
    Q = deque()
    flag = True
    Q.append(root)
    while Q and flag:
        n = len(Q)
        for i in range(n):
            temp = Q.popleft()
            if temp.left:
                if temp.left.val==key:
                    flag = False
                Q.append(temp.left)
            if temp.right:
                if temp.right.val==key:
                    flag = False
                Q.append(temp.right)
    if not Q:
        return []
    return Q

key = int(input())
arr = [int(i) for i in input().split()]
root = buildTree(arr)
add = findSiblings(root,key)
res = []
if add:
    for i in add:
        res.append(i.val)
    print(res) 
else:
    print(-1) 